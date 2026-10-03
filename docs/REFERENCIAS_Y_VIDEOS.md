# Referencias y videos de apoyo

Consulta: 2 de octubre de 2026. Las guías contienen un diseño de laboratorio propio. Las referencias documentan plataformas, protocolos y equipos; no garantizan que una función esté habilitada en el tenant del grupo.

## Videos

| Material | Departamento | Qué revisar |
|---|---|---|
| [OneLogin: Groups, Roles, and Mappings, Oh My!](https://www.onelogin.com/video/groups-roles-and-mappings-oh-my) | Dirección, RRHH, IAM y Auditoría | Diferencia entre grupos, roles y asignación automática |
| [OneLogin: Identity Lifecycle Management, parte 2](https://www.onelogin.com/resource-center/videos/getting-started-with-identity-lifecycle-management-pt-2) | RRHH, IAM, SOC y Auditoría | Aprovisionamiento, retiro, reglas y aprobación |
| [Microsoft: agregar usuarios y licencias, videos integrados](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/add-users?view=o365-worldwide) | TI, RRHH y Auditoría | Alta individual y varias cuentas |
| [Microsoft: Reset user passwords](https://www.youtube.com/watch?v=8ShQqMZmhRg) | TI | Restablecimiento de contraseña |
| [Frigate + Docker: Self Hosted CCTV System](https://www.youtube.com/watch?v=KMD72_Wfp3E) | TI, Seguridad Física y SOC | Orientación visual de instalación e interfaz |
| [Arduino RFID Sensor, MFRC522](https://www.youtube.com/watch?v=CQLPo7xqORQ) | Seguridad Física | Uso del lector, únicamente si coincide el hardware |

Los videos externos pueden usar versiones anteriores. El ejemplo Frigate de este paquete fija 0.17.1; no copiar su configuración de grabación desde un video viejo. La parte de detección de objetos, MQTT y Home Assistant del video no es necesaria para el proyecto. En RFID, prevalecen la hoja de datos y los niveles eléctricos del módulo real.

Los enlaces de video fueron localizados por título, canal o página del fabricante. Algunas páginas no permitieron reproducción automatizada; no se ha verificado cada minuto del contenido. Si un video no abre, utilizar la referencia escrita del mismo tema.

## NVR y cámaras

- [Frigate, repositorio y licencia](https://github.com/blakeblackshear/frigate).
- [Versiones Frigate](https://github.com/blakeblackshear/frigate/releases): imagen 0.17.1 utilizada en el ejemplo.
- [Instalación](https://docs.frigate.video/frigate/installation/): contenedor, directorios y puertos.
- [Configuración](https://docs.frigate.video/configuration/config/): archivo YAML.
- [Cámaras](https://docs.frigate.video/configuration/cameras/): entradas y funciones de video.
- [Grabación](https://docs.frigate.video/configuration/record/): grabación continua, retención y exportación.
- [Presets FFmpeg](https://docs.frigate.video/configuration/ffmpeg_presets/): lectura RTSP/MJPEG y formato de grabación.
- [Autenticación](https://docs.frigate.video/configuration/authentication/): cuentas y puerto protegido.
- [TLS](https://docs.frigate.video/configuration/tls/): certificados del NVR.
- [Problemas de grabación](https://docs.frigate.video/troubleshooting/recordings/): diagnóstico de video no guardado.
- [IP Webcam en Google Play](https://play.google.com/store/apps/details?id=com.pas.webcam): cámara Android y transmisión local.
- [IP Camera Lite en App Store](https://apps.apple.com/us/app/ip-camera-lite/id1013455241): cámara iPhone, RTSP y limitaciones Lite.

## OneLogin

- [Conectar aplicación OIDC](https://developers.onelogin.com/docs/openid-connect/connect-to-onelogin/).
- [Configuración del proveedor OIDC](https://developers.onelogin.com/docs/openid-connect/api/provider-config/).
- [Ejemplos oficiales OIDC](https://developers.onelogin.com/docs/openid-connect/samples/).
- [Definir esquema SCIM](https://developers.onelogin.com/docs/scim/define-user-schema/).
- [Implementar API SCIM](https://developers.onelogin.com/docs/scim/implement-scim-api/).
- [Crear aplicación SCIM de prueba](https://developers.onelogin.com/docs/scim/create-app/).
- [Introducción al aprovisionamiento](https://onelogin.service-now.com/kb?id=kb_article_view&sysparm_article=KB0010298).
- [Automatización con mappings y rules](https://onelogin.service-now.com/kb?id=kb_article_view&sysparm_article=KB0011995).
- [Agregar MFA](https://www.onelogin.com/getting-started/free-trial-plan/add-mfa).
- [Políticas de usuario](https://support.onelogin.com/kb/4271392/user-policies).

## Microsoft 365

- [Agregar usuarios y licencias](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/add-users?view=o365-worldwide).
- [Restablecer contraseñas](https://learn.microsoft.com/en-gb/microsoft-365/admin/add-users/reset-passwords?view=o365-worldwide).
- [Configurar MFA](https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/set-up-multi-factor-authentication).
- [Valores predeterminados de seguridad](https://learn.microsoft.com/en-us/entra/fundamentals/security-defaults).
- [Registrar verificación adicional](https://support.microsoft.com/en-us/office/account-management/set-up-your-microsoft-365-sign-in-for-multi-factor-authentication).
- [Auditoría Entra](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-audit-logs).
- [Bloquear acceso al salir un empleado](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/remove-former-employee-step-1?view=o365-worldwide).

## Instalación, aplicación y hardware

- [Docker Engine en Ubuntu](https://docs.docker.com/engine/install/ubuntu/).
- [Cloudflare Quick Tunnels](https://developers.cloudflare.com/tunnel/get-started/quick-tunnels/).
- [Authlib, cliente Flask](https://github.com/authlib/authlib/blob/main/docs/client/flask.rst).
- [mkcert](https://github.com/FiloSottile/mkcert).
- [Biblioteca Arduino MFRC522](https://github.com/miguelbalboa/rfid).
- [Arduino IDE](https://www.arduino.cc/en/software).

## Informe

- [Plantillas IEEE](https://www.ieee.org/conferences/publishing/templates.html).
- [Primer proyecto en Overleaf](https://docs.overleaf.com/getting-started/your-first-project).
