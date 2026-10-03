# Editar y compilar los PDF

Los PDF públicos se generan con XeLaTeX, en blanco y negro y Times New Roman. La fuente está incrustada: leer un PDF no requiere instalarla. Para recompilar, instalar la fuente en la laptop y una distribución TeX Live con los paquetes necesarios.

Paquetes: babel español, fontspec, geometry, longtable, array, booktabs, fvextra, enumitem, fancyhdr, needspace, hyperref, xurl, tikz y graphicx. No se incluyen archivos sueltos de fuentes dentro del repositorio.

1. Editar el `.md` para la lectura en GitHub y el `.tex` correspondiente para el PDF.
2. Mantener los ejemplos genéricos; no usar el control privado como fuente.
3. Ejecutar la compilación desde la raíz:

```bash
python3 scripts/compile_docs.py
```

El comando compila dos veces los diez documentos y el cuaderno de diagramas, revisa errores de LaTeX y elimina archivos auxiliares. No instala fuentes ni paquetes. Si falta Times New Roman, la compilación se detiene y muestra el error; no sustituye silenciosamente la fuente.

Para un archivo específico:

```bash
cd docs/Guias
xelatex -interaction=nonstopmode -halt-on-error 08_Uso_de_Python.tex
xelatex -interaction=nonstopmode -halt-on-error 08_Uso_de_Python.tex
```

4. Abrir cada PDF modificado y revisar tablas, comandos, márgenes y enlaces.
5. Ejecutar el control de contenido público y revisar `git diff` antes de subir.

Los diagramas tienen fuentes SVG para lectura en GitHub y fuentes TikZ dentro de LaTeX. El PDF `Diagramas_completos.pdf` reúne los trece. Si cambia un diagrama, actualizar también su sección en el cuaderno; el script no convierte SVG ni Markdown automáticamente.
