"""Datos y permisos de la aplicación de laboratorio."""
import json
import sqlite3
import uuid
from datetime import datetime, timezone
from pathlib import Path

PERMISSIONS = {
    'admin': {'consulta', 'mantenimiento', 'admin', 'registros'},
    'mantenimiento': {'consulta', 'mantenimiento'},
    'auditor': {'consulta', 'registros'},
    'consulta': {'consulta'},
    'sin_acceso': set(),
}


def utc_now():
    return datetime.now(timezone.utc).isoformat()


class Store:
    def __init__(self, path):
        self.path = str(path)
        Path(self.path).parent.mkdir(parents=True, exist_ok=True)
        with self.connect() as db:
            db.execute('CREATE TABLE IF NOT EXISTS users (id TEXT PRIMARY KEY, username TEXT UNIQUE NOT NULL, payload TEXT NOT NULL, oidc_sub TEXT UNIQUE)')
            db.execute('CREATE TABLE IF NOT EXISTS events (time TEXT, user TEXT, action TEXT, result TEXT)')

    def connect(self):
        db = sqlite3.connect(self.path, timeout=15)
        db.row_factory = sqlite3.Row
        return db

    def resource(self, row):
        return json.loads(row['payload']) if row else None

    def get(self, user_id):
        with self.connect() as db:
            return self.resource(db.execute('SELECT * FROM users WHERE id=?', (user_id,)).fetchone())

    def by_name(self, username):
        with self.connect() as db:
            return self.resource(db.execute('SELECT * FROM users WHERE username=?', (username.lower().strip(),)).fetchone())

    def all(self):
        with self.connect() as db:
            return [self.resource(r) for r in db.execute('SELECT * FROM users ORDER BY username')]

    def save(self, payload, user_id=None):
        previous = self.get(user_id) if user_id else None
        data = dict(previous or {})
        data.update(payload)
        username = str(data.get('userName', '')).strip().lower()
        if not username or '@' not in username:
            raise ValueError('userName debe ser un correo de laboratorio')
        active = data.get('active', True)
        if isinstance(active, str):
            if active.lower() not in ('true', 'false'):
                raise ValueError('active debe ser true o false')
            active = active.lower() == 'true'
        if not isinstance(active, bool):
            raise ValueError('active debe ser true o false')
        data['active'] = active
        data['userName'] = username
        data['id'] = user_id or str(uuid.uuid4())
        data.setdefault('schemas', ['urn:scim:schemas:core:1.0'])
        data['meta'] = {'resourceType': 'User', 'lastModified': utc_now()}
        with self.connect() as db:
            db.execute('INSERT INTO users(id,username,payload) VALUES(?,?,?) ON CONFLICT(id) DO UPDATE SET username=excluded.username,payload=excluded.payload', (data['id'], username, json.dumps(data)))
        self.event(data['id'], 'SCIM_CREATE' if previous is None else 'SCIM_UPDATE', 'OK')
        return data

    def remove(self, user_id):
        with self.connect() as db:
            db.execute('DELETE FROM users WHERE id=?', (user_id,))
        self.event(user_id, 'SCIM_DELETE', 'OK')

    def bind_identity(self, user_id, subject):
        with self.connect() as db:
            row = db.execute('SELECT oidc_sub FROM users WHERE id=?', (user_id,)).fetchone()
            if row is None or (row['oidc_sub'] and row['oidc_sub'] != subject):
                return False
            try:
                db.execute('UPDATE users SET oidc_sub=? WHERE id=?', (subject, user_id))
            except sqlite3.IntegrityError:
                return False
        return True

    def permitted(self, user_id, action):
        user = self.get(user_id)
        return bool(user and user.get('active', False) and action in PERMISSIONS.get(user.get('title', 'sin_acceso'), set()))

    def event(self, user, action, result):
        with self.connect() as db:
            db.execute('INSERT INTO events VALUES(?,?,?,?)', (utc_now(), user, action, result))

    def events(self):
        with self.connect() as db:
            return [dict(r) for r in db.execute('SELECT * FROM events ORDER BY rowid DESC LIMIT 100')]
