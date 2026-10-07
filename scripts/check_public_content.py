"""Check tracked/public artifacts; this is a guard, not a universal PII detector."""
from pathlib import Path
import csv
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
SECRET_PATTERNS = (
    re.compile(r'(?:gh[pousr]_[A-Za-z0-9]{25,}|github_pat_[A-Za-z0-9_]{30,})'),
    re.compile(r'AKIA[A-Z0-9]{16}'),
    re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----'),
    re.compile(r'eyJ[A-Za-z0-9_-]{15,}\.[A-Za-z0-9_-]{15,}\.[A-Za-z0-9_-]{15,}'),
    re.compile(r'(?:https?|rtsp)://[^\s/:{}]+:[^\s/@{}]+@'),
    re.compile(r'docs\.google\.com/(?:spreadsheets|document)/d/[^\s/)]+'),
    re.compile(r'(?:/' + r'home/[^/\s]+/|[A-Za-z]:\\Users\\[^\\\s]+\\)'),
)
EMAIL = re.compile(r'[\w.+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}')
FORBIDDEN_EXTENSIONS = {'.db','.sqlite','.sqlite3','.xlsx','.xls','.zip','.pem','.key','.p12','.pfx','.mp4','.mkv','.avi','.jpg','.jpeg','.png','.gif','.webp','.log'}
FORBIDDEN_DIRS = {'privado','private','evidencias','evidence','data','media','certs','.venv','__pycache__'}
ALLOWED_TOP = {'README.md','CONTRIBUTING.md','PRIVACIDAD.md','GUIA_USO_DASHBOARD_RESPONSABLES.pdf','.gitignore','docs','Implementacion','Plantillas','scripts','.github'}

def text_issues(text):
    result=[]
    if any(pattern.search(text) for pattern in SECRET_PATTERNS):
        result.append('Patrón de secreto, vínculo privado o ruta personal')
    for email in EMAIL.findall(text):
        domain=email.rsplit('@',1)[1].lower()
        if not (domain.endswith(('.test','.example')) or domain=='users.noreply.github.com'):
            result.append('Correo fuera de dominios ficticios/noreply')
            break
    return result

def file_issues(path):
    rel=path.relative_to(ROOT);problems=[]
    if rel.parts[0] not in ALLOWED_TOP:problems.append('Ruta no incluida en el árbol público permitido')
    if path.is_symlink():return problems+['Enlace simbólico no permitido']
    if set(rel.parts)&FORBIDDEN_DIRS:problems.append('Archivo en carpeta operativa/privada')
    if path.suffix.lower() in FORBIDDEN_EXTENSIONS:problems.append('Tipo de archivo operativo o sensible')
    if path.name.startswith('.env') and path.name!='.env.example':problems.append('Configuración privada .env')
    if path.name in {'config.yml','config.yaml'}:problems.append('Configuración operativa; publicar únicamente el ejemplo')
    if path.suffix=='.csv':
        if rel.parts[0]!='Plantillas':problems.append('CSV fuera de las plantillas públicas')
        rows=list(csv.reader(path.open(encoding='utf-8-sig')))
        if len(rows)!=1:problems.append('La plantilla debe contener solo encabezados, sin filas de datos')
    if path.suffix=='.pdf':
        from pypdf import PdfReader
        pdf=PdfReader(path)
        text='\n'.join(page.extract_text() or '' for page in pdf.pages)
        metadata=pdf.metadata or {}
        if str(metadata.get('/Author','')).strip():problems.append('PDF con autor en metadatos')
        if pdf.attachments:problems.append('PDF con archivos adjuntos')
        for page in pdf.pages:
            for annotation in page.get('/Annots',[]):
                obj=annotation.get_object();action=obj.get('/A',{})
                if action: text+='\n'+str(action.get('/URI',''))
        text+='\n'+'\n'.join(str(x) for x in metadata.values())
    elif path.suffix.lower() in {'.md','.tex','.svg','.py','.ino','.json','.yml','.yaml','.csv','.txt'} or path.name in {'.gitignore','.env.example'}:
        text=path.read_text(encoding='utf-8-sig')
    else:return problems+['Formato sin revisión automatizada; requiere ampliar la política']
    problems.extend(text_issues(text))
    if path.name=='.env.example':
        for line in text.splitlines():
            if '=' not in line or line.lstrip().startswith('#'):continue
            key,value=line.split('=',1)
            if any(word in key.upper() for word in ('SECRET','TOKEN','PASSWORD')) and 'REEMPLAZAR' not in value:
                problems.append('Secreto en ejemplo sin marcador REEMPLAZAR')
    return problems

def public_files():
    # Git's tracked set is the publication boundary. Before initialization, inspect the tree.
    result=subprocess.run(['git','ls-files','-z','--cached','--others','--exclude-standard'],cwd=ROOT,capture_output=True)
    if result.returncode==0:
        return sorted(ROOT / item.decode('utf-8') for item in result.stdout.split(b'\0') if item)
    return sorted(p for p in ROOT.rglob('*') if p.is_file() and '.git' not in p.parts and not set(p.relative_to(ROOT).parts)&FORBIDDEN_DIRS and p.suffix not in {'.aux','.out','.log'})

def main():
    failures=[];files=public_files()
    for path in files:
        if not path.exists():continue
        try:issues=file_issues(path)
        except Exception:issues=['No se pudo revisar el archivo; corregir antes de publicar']
        for issue in issues:failures.append(f'{path.relative_to(ROOT)}: {issue}')
    if failures:
        print('\n'.join(failures));return 1
    print(f'Contenido público revisado: {len(files)} archivos. Sin hallazgos de los patrones comprobados.')
    return 0

if __name__=='__main__':sys.exit(main())
