"""Compile public standalone LaTeX documents with installed XeLaTeX/fonts."""
from pathlib import Path
import shutil
import subprocess

root = Path(__file__).resolve().parents[1]
if not shutil.which('xelatex'):
    raise SystemExit('Instalar XeLaTeX antes de compilar.')
files = sorted((root / 'docs').glob('*.tex'))
files += sorted((root / 'docs/Guias').glob('*.tex'))
files += [root / 'docs/Diagramas/Diagramas_completos.tex']
for path in files:
    for _ in range(2):
        result = subprocess.run(
            ['xelatex', '-interaction=nonstopmode', '-halt-on-error', path.name],
            cwd=path.parent, capture_output=True, text=True,
        )
        if result.returncode:
            print(result.stdout[-3000:])
            raise SystemExit(f'Error de compilación: {path.name}')
    log = path.with_suffix('.log').read_text(errors='replace')
    if 'Overfull \\hbox' in log or 'Missing character:' in log:
        raise SystemExit(f'Revisar texto desbordado o caracteres: {path.name}')
    for suffix in ('.aux', '.out', '.log'):
        path.with_suffix(suffix).unlink(missing_ok=True)
    print(f'PDF creado: {path.relative_to(root).with_suffix(".pdf")}')
