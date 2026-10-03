# Manual de implementación de IDENTITY ACCESS LAB

Fecha: 2 de octubre de 2026. Este paquete público explica cómo construir un laboratorio genérico. Todos los identificadores y direcciones de ejemplo son ficticios. Los pasos no significan que las plataformas ya estén configuradas.

## Decisiones del montaje

- NVR virtual autorizado: **Frigate**, software de código abierto. La configuración incluida usa la versión 0.17.1 para que todos trabajen con la misma base.
- Cámaras: teléfonos Android y iPhone. La ruta Android usa IP Webcam y video MJPEG; la ruta iPhone usa IP Camera Lite y video RTSP/H.264. Las aplicaciones de teléfono no se presentan como software de código abierto; ese requisito se aplica al NVR.
- Identidades digitales: **OneLogin obligatorio**, con inicio de sesión real y una conexión para crear y retirar cuentas de la aplicación.
- Microsoft 365: administración de cuentas, licencias, roles, contraseña, MFA y registros en un entorno de práctica autorizado.
- Servidor y NVR: comandos para Ubuntu 24.04 LTS de 64 bits. Si la laptop usa Windows, preparar una máquina virtual Ubuntu o conseguir una laptop Linux; no ejecutar comandos de Ubuntu en PowerShell.
- Dos laptops disponibles por departamento: 14 equipos con funciones asignadas. Las demás apoyan desarrollo, documentación y pruebas.
- RFID: modelo pendiente. El ejemplo incluido es únicamente para Arduino Uno + MFRC522. Identificar el equipo antes de cablear.

## Archivos

Las ocho guías están en `Guias/`. Los diagramas están separados en `Diagramas/`, en SVG y PDF, con fuentes LaTeX. El código y las configuraciones están en `Implementacion/`. Los formularios y listas están en `Plantillas/`. `REFERENCIAS_Y_VIDEOS.md` reúne documentación y videos vinculados desde cada guía.

## Orden de trabajo

1. Dirección y RRHH corrigen la lista de integrantes y acuerdan responsables.
2. TI prepara red, equipos Ubuntu y conexión a internet.
3. Seguridad Física identifica el lector y monta cámaras y NVR con apoyo de TI.
4. TI prepara la aplicación. IAM configura OneLogin y conecta inicio de sesión y altas/bajas.
5. TI configura Microsoft 365; IAM coordina la segunda verificación.
6. SOC prepara monitoreo y consulta de registros.
7. Auditoría ejecuta pruebas con todos los equipos.
8. Se realiza el recorrido completo y se prepara la entrega.

No esperen a terminar todo el RFID para iniciar red, cámaras y cuentas. La integración de OneLogin depende de que la aplicación y su dirección HTTPS funcionen primero.

## Distribución propuesta

31 puestos genéricos: Dirección 3, RRHH 3, TI 7, IAM 5, SOC 5, Seguridad Física 5 y Auditoría 3. Los puestos no representan personas identificadas. Las asignaciones y cualquier cambio se mantienen en un registro privado.

## Equipos por área

| Área | Laptop 1 | Laptop 2 |
|---|---|---|
| Dirección | Calendario, pendientes y control del grupo | Guion, presentación y copia de entregables |
| RRHH | Registro de empleados | Solicitudes de alta, cambio y baja |
| TI | Servidor de aplicación y conexión HTTPS | Red, Microsoft 365 y soporte |
| IAM | Consola OneLogin | Pruebas de usuarios y permisos |
| SOC | Cámaras desde el navegador | Registros, incidentes y evidencias |
| Seguridad Física | Microcontrolador y registro RFID | Frigate y almacenamiento de video |
| Auditoría | Lista de pruebas | Informe, referencias y evidencias |

Las funciones son asignaciones propuestas, no una exigencia de mantener todas las laptops encendidas a la vez. El NVR y servidor deben permanecer encendidos durante las pruebas continuas.

## Direcciones de ejemplo

| Equipo | Dirección prevista |
|---|---|
| Router/punto de acceso | 10.31.0.1 |
| Servidor TI | 10.31.0.10 |
| NVR | 10.31.0.20 |
| Laptop RFID | 10.31.0.21 |
| Android de entrada | 10.31.0.31 |
| iPhone interior | 10.31.0.32 |
| SOC | 10.31.0.40 y 10.31.0.41 |

Esta red es una propuesta. Si el router usa otra red, TI actualiza direcciones, diagramas y configuraciones. No asignar direcciones de ejemplo que no pertenezcan a la red real. Preferir reservas de dirección en el router.

## Qué representa cada sistema

- La tarjeta y el LED deciden el paso físico supervisado.
- Frigate guarda video y permite consultarlo desde laptop y móvil.
- OneLogin comprueba la identidad del usuario y aplica su política de MFA.
- La aplicación comprueba qué acciones puede realizar el usuario.
- La conexión SCIM transmite a la aplicación altas, cambios y bajas desde OneLogin. SCIM es el mecanismo de sincronización, no otro proveedor de identidades.
- Microsoft 365 administra las cuentas corporativas del ejercicio. En este diseño no se federan ni sincronizan automáticamente Microsoft 365 y OneLogin. Se relacionan mediante el registro de RRHH y el mismo correo de laboratorio. Cambiar la contraseña en Microsoft 365 no cambia automáticamente la de OneLogin.

Se usan dos conectores en OneLogin: uno OIDC para iniciar sesión y uno SCIM Core para sincronizar usuarios. El conector SCIM incluye “SAML” en su nombre comercial, pero aquí solo se usa su función de aprovisionamiento; el inicio de sesión de la aplicación es OIDC.

## Datos que hay que completar

Dirección registra sistemas operativos, modelos del lector y placa, acceso a tenants, licencias, puerto/dirección de cada cámara y duración acordada de la prueba 24/7. La autorización del NVR virtual ya está confirmada. La adaptación específica de transceptores de video se debe dejar registrada por escrito para que el informe explique cómo se cubrió o sustituyó ese punto.

## Uso de comandos y verificación

- Copiar el paquete a las laptops designadas. Las rutas `~/lab-runtime/` se refieren a la carpeta del proyecto en esas laptops.
- Reemplazar todo texto `REEMPLAZAR` antes de iniciar servicios.
- No compartir `.env`, claves privadas, contraseñas ni códigos de MFA en evidencias.
- Ejecutar cada bloque en el equipo indicado y revisar el resultado antes del siguiente paso.
- El código base tiene pruebas locales de permisos, cambio de rol, baja y vínculo de identidad. La conexión real con OneLogin, las cámaras y el RFID requiere sus cuentas y equipos; no se considera probada en este paquete.

Consultar [referencias y videos](REFERENCIAS_Y_VIDEOS.md). Los videos son apoyo visual; las configuraciones versionadas y las fuentes oficiales resuelven diferencias de menús o versiones.
