"""Aplicación de práctica: OneLogin OIDC y aprovisionamiento SCIM Core 1.0.
No incluye acceso alternativo con contraseña local.
"""
import hmac
import os
import re
import secrets
import sqlite3
from datetime import timedelta
from functools import wraps
from flask import Flask, abort, jsonify, redirect, render_template_string, request, session
from authlib.integrations.flask_client import OAuth
from store import Store

app = Flask(__name__)
app.secret_key = os.environ['APP_SECRET']
BASE = os.environ['APP_BASE_URL'].rstrip('/')
SCIM_TOKEN = os.environ['SCIM_TOKEN']
if len(app.secret_key) < 32 or len(SCIM_TOKEN) < 32 or not BASE.startswith('https://'):
    raise RuntimeError('Configura secretos de al menos 32 caracteres y APP_BASE_URL HTTPS')
app.config.update(SESSION_COOKIE_SECURE=True, SESSION_COOKIE_HTTPONLY=True, SESSION_COOKIE_SAMESITE='Lax', PERMANENT_SESSION_LIFETIME=timedelta(minutes=15), MAX_CONTENT_LENGTH=65536)
store = Store(os.environ.get('APP_DB', 'data/lab.sqlite'))
oauth = OAuth(app)
oauth.register(name='onelogin', client_id=os.environ['OIDC_CLIENT_ID'], client_secret=os.environ['OIDC_CLIENT_SECRET'], server_metadata_url=os.environ['OIDC_METADATA_URL'], client_kwargs={'scope': 'openid profile email'})


def error(message, status):
    return jsonify({'schemas': ['urn:scim:schemas:core:1.0'], 'detail': message, 'status': str(status)}), status


def scim_required(fn):
    @wraps(fn)
    def wrapped(*args, **kwargs):
        token = request.headers.get('Authorization', '')
        if not hmac.compare_digest(token, 'Bearer ' + SCIM_TOKEN):
            return error('No autorizado', 401)
        return fn(*args, **kwargs)
    return wrapped


def allowed(action):
    def decorator(fn):
        @wraps(fn)
        def wrapped(*args, **kwargs):
            uid = session.get('uid')
            if not uid:
                return redirect('/login')
            if not store.permitted(uid, action):
                store.event(uid, action, 'DENEGADO')
                abort(403)
            if request.method == 'POST' and not hmac.compare_digest(request.form.get('csrf', ''), session.get('csrf', '')):
                abort(400)
            store.event(uid, action, 'PERMITIDO')
            return fn(*args, **kwargs)
        return wrapped
    return decorator


@app.get('/health')
def health():
    return jsonify({'status': 'ok'})


@app.get('/')
def home():
    uid = session.get('uid')
    user = store.get(uid) if uid else None
    if user and not user.get('active', False):
        session.clear()
        user = None
    if not user:
        return '<h1>Servidor IDENTITY ACCESS LAB</h1><p><a href="/login">Iniciar sesión con OneLogin</a></p>'
    session.setdefault('csrf', secrets.token_urlsafe(32))
    return render_template_string('''<!doctype html><meta charset="utf-8"><title>Servidor IDENTITY ACCESS LAB</title>
    <h1>Servidor IDENTITY ACCESS LAB</h1><p>Usuario: {{user.userName}} | Rol: {{user.title}}</p>
    <p><a href="/consulta">Consultar estado</a> · <a href="/registros">Ver registros</a></p>
    <form action="/mantenimiento" method="post"><input type="hidden" name="csrf" value="{{csrf}}"><button>Ejecutar mantenimiento de prueba</button></form>
    <form action="/admin" method="post"><input type="hidden" name="csrf" value="{{csrf}}"><button>Administrar configuración de prueba</button></form>
    <form action="/logout" method="post"><input type="hidden" name="csrf" value="{{csrf}}"><button>Cerrar sesión de la aplicación</button></form>''', user=user, csrf=session['csrf'])


@app.get('/login')
def login():
    return oauth.onelogin.authorize_redirect(BASE + '/auth/callback', prompt='login')


@app.get('/auth/callback')
def callback():
    try:
        token = oauth.onelogin.authorize_access_token()
        identity = token.get('userinfo')
        if not identity or not identity.get('sub') or not identity.get('email'):
            abort(403)
        user = store.by_name(identity['email'])
        if not user or not user.get('active', False) or not store.bind_identity(user['id'], str(identity['sub'])):
            store.event('desconocido', 'LOGIN', 'DENEGADO')
            abort(403)
        session.clear()
        session['uid'] = user['id']
        session['csrf'] = secrets.token_urlsafe(32)
        session.permanent = True
        store.event(user['id'], 'LOGIN_ONELOGIN', 'PERMITIDO')
        return redirect('/')
    except Exception:
        app.logger.warning('Inicio de sesión no completado; revisar configuración y eventos de OneLogin')
        abort(403)


@app.get('/consulta')
@allowed('consulta')
def consult():
    return '<h1>Consulta permitida</h1><p>Servidor de práctica disponible.</p><a href="/">Volver</a>'


@app.post('/mantenimiento')
@allowed('mantenimiento')
def maintenance():
    return '<h1>Mantenimiento permitido</h1><p>Operación simulada registrada. No modifica el sistema operativo.</p><a href="/">Volver</a>'


@app.post('/admin')
@allowed('admin')
def admin():
    return '<h1>Administración permitida</h1><p>Operación simulada registrada.</p><a href="/">Volver</a>'


@app.get('/registros')
@allowed('registros')
def records():
    return jsonify(store.events())


@app.post('/logout')
def logout():
    if not session.get('uid') or not hmac.compare_digest(request.form.get('csrf', ''), session.get('csrf', '')):
        abort(400)
    store.event(session['uid'], 'LOGOUT_APP', 'OK')
    session.clear()
    return redirect('/')


@app.route('/scim/v1/Users', methods=['GET', 'POST'])
@scim_required
def users():
    if request.method == 'GET':
        query = request.args.get('filter', '')
        if query:
            match = re.fullmatch(r'userName\s+eq\s+"([^"]+)"', query, re.IGNORECASE)
            if not match:
                return error('Solo se admite filtro userName eq "correo"', 400)
            found = store.by_name(match.group(1))
            resources = [found] if found else []
        else:
            resources = store.all()
        start = max(1, request.args.get('startIndex', 1, type=int))
        count = max(0, min(100, request.args.get('count', 100, type=int)))
        page = resources[start-1:start-1+count]
        return jsonify({'schemas': ['urn:scim:schemas:core:1.0'], 'totalResults': len(resources), 'startIndex': start, 'itemsPerPage': len(page), 'Resources': page})
    try:
        data = store.save(request.get_json(force=True))
        return jsonify(data), 201, {'Location': BASE + '/scim/v1/Users/' + data['id']}
    except sqlite3.IntegrityError:
        return error('Usuario duplicado', 409)
    except (ValueError, TypeError):
        return error('Datos de usuario no válidos', 400)


@app.route('/scim/v1/Users/<user_id>', methods=['GET', 'PUT', 'PATCH', 'DELETE'])
@scim_required
def user_resource(user_id):
    previous = store.get(user_id)
    if not previous:
        return error('Usuario no encontrado', 404)
    if request.method == 'GET':
        return jsonify(previous)
    if request.method == 'DELETE':
        store.remove(user_id)
        return '', 204
    try:
        payload = request.get_json(force=True)
        if request.method == 'PATCH' and 'Operations' in payload:
            changes = {}
            for operation in payload['Operations']:
                if operation.get('op', '').lower() not in ('replace', 'add'):
                    return error('Operación PATCH no admitida', 400)
                path = operation.get('path')
                if path in ('active', 'title', 'userName', 'externalId'):
                    changes[path] = operation.get('value')
                elif path is None and isinstance(operation.get('value'), dict):
                    changes.update(operation['value'])
                else:
                    return error('Ruta PATCH no admitida', 400)
            payload = changes
        return jsonify(store.save(payload, user_id))
    except sqlite3.IntegrityError:
        return error('Usuario duplicado', 409)
    except (ValueError, TypeError):
        return error('Datos de usuario no válidos', 400)


@app.get('/scim/v1/Groups')
@scim_required
def groups():
    return jsonify({'schemas': ['urn:scim:schemas:core:1.0'], 'totalResults': 0, 'startIndex': 1, 'itemsPerPage': 0, 'Resources': []})
