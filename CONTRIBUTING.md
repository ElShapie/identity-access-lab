# Cómo colaborar

## Consultar material

No es necesario tener cuenta GitHub para leer o descargar el repositorio público. Empezar por el README y abrir la guía del área. Las asignaciones de personas se acuerdan en un canal privado.

## Proponer cambios desde GitHub

1. Abrir un archivo Markdown y pulsar editar. Si no hay permisos de escritura, GitHub propone una copia mediante fork.
2. Cambiar instrucciones o ejemplos sin incorporar información real.
3. Usar un título que describa la corrección, por ejemplo `Aclarar comprobación del puerto de cámara`.
4. Crear un pull request y completar la plantilla.
5. Esperar la revisión del responsable y el resultado de las comprobaciones.

No incluir nombres, institución, capturas identificables ni configuraciones reales en comentarios, títulos, ramas o archivos.

## Cambiar archivos desde una laptop

```bash
git clone https://github.com/ElShapie/identity-access-lab.git
cd identity-access-lab
git config user.name "Lab Contributor"
git config user.email "documentation@users.noreply.github.com"
git config commit.gpgsign false
git switch -c docs/mejora-guia
```

Editar únicamente los archivos necesarios. Si cambia una guía, actualizar Markdown, LaTeX y PDF correspondientes; ver `docs/COMPILAR_LATEX.md`. No sustituir ejemplos por valores reales del laboratorio.

```bash
python3 -m unittest discover -s Implementacion/app -p 'test_store.py' -v
python3 scripts/check_public_content.py
git status --short
git add docs/Guias/03_TI.md
git diff --cached
git commit -m "Aclarar pasos de instalación de TI"
git push -u origin docs/mejora-guia
```

El archivo de `git add` es un ejemplo: agregar explícitamente cada archivo revisado que corresponda. El push directo requiere permisos de escritura. Si se trabaja en un fork, apuntar `origin` a ese fork y abrir el pull request hacia este repositorio.

## Revisar un cambio

Comprobar que los comandos tienen equipo de ejecución y resultado esperado, que la documentación y el PDF coinciden, que se conservan fuentes/referencias y que no aparecen datos personales. Verificar los resultados automáticos antes de integrar.

La persona administradora puede agregar colaboradores desde **Settings → Collaborators**. No se agregan personas automáticamente. Para el control del proyecto, usar Issues por tareas genéricas y etiquetas por departamento, sin datos operativos ni nombres en su contenido.
