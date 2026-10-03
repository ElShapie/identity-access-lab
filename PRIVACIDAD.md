# Reglas para conservar el repositorio sin datos sensibles

## Qué se publica

Guías, código, diagramas de ejemplo, referencias oficiales, formularios vacíos y documentación técnica. Los identificadores de demostración son ficticios. Las rutas `~/identity-access-lab/` describen carpetas de instalación propuestas, no rutas de una computadora personal.

## Qué se mantiene fuera

Nombres y apellidos, institución, matrículas, lista de participantes, correos personales/corporativos reales, teléfonos, direcciones, UID reales, propietarios de equipos, tenants identificables, credenciales, secretos, códigos MFA, certificados privados, bases de datos, registros de acceso, video, fotografías y capturas con información visible. No cargar el PDF del enunciado ni hojas de cálculo del grupo.

Las plantillas en `Plantillas/` contienen solo encabezados. Guardar una copia completada fuera del repositorio; la carpeta `privado/` está ignorada, pero una carpeta externa ofrece separación adicional. No usar `git add -f` para forzar archivos ignorados.

## Antes de un commit

1. Usar únicamente nombres de puestos e identidades ficticias.
2. Revisar el texto, capturas, enlaces y propiedades del archivo.
3. Revisar `git status --short` y `git diff --cached`.
4. Ejecutar `python3 scripts/check_public_content.py`.
5. Pedir una revisión humana de la documentación modificada.
6. Publicar el cambio mediante pull request.

La revisión automatizada busca patrones de secretos, enlaces privados, metadatos, archivos operativos y filas pobladas en plantillas. No reconoce todos los nombres propios ni toda información identificable; la revisión humana sigue siendo necesaria. Las comprobaciones de GitHub pueden señalar un cambio después de que se haya subido: no sustituyen la revisión antes del push.

## Identidad de los commits

Git registra autor y correo. En este repositorio el commit inicial usa una identidad genérica. Para futuros commits, configurar únicamente este repositorio:

```bash
git config user.name "Lab Contributor"
git config user.email "documentation@users.noreply.github.com"
git config commit.gpgsign false
```

También puede usarse el correo noreply que entrega GitHub y un alias, si se desea conservar atribución. No cambiar la configuración global si otros proyectos necesitan otra identidad. GitHub muestra cuentas propietarias, colaboradores y autores de pull requests; estas reglas no convierten la plataforma en anónima.

## Si se publica algo sensible

Detener nuevos envíos del archivo. Si hay una credencial, revocarla o cambiarla de inmediato. Eliminarla de la versión actual no la elimina del historial. Coordinar la limpieza de historial, clones, forks y cachés según la [guía oficial de GitHub](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository). No pegar el secreto o los datos afectados en un Issue público para explicar el incidente.
