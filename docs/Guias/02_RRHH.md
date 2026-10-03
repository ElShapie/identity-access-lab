# Recursos Humanos

## Objetivo y puestos

Mantener el registro de empleados y comunicar altas, cambios y bajas. RRHH define la situación laboral del escenario; el dueño de cada recurso aprueba sus accesos.

RRHH tiene tres funciones: validar solicitudes, preparar altas y administrar cambios y bajas. TI mantiene el registro técnico validado por RRHH. Los nombres y correos reales se guardan únicamente en el control privado.

Laptop 1: registro. Laptop 2: solicitudes y seguimiento.

## Paso 1. Preparar registro común

1. Copiar `Plantillas/empleados.csv` a la carpeta compartida.
2. Mantener un ID EMP por integrante. No cambiar ID al cambiar departamento.
3. Escribir nombre, puesto, departamento y estado.
4. Coordinar con TI un correo de laboratorio. Usar exactamente el mismo correo como identidad de la aplicación y OneLogin.
5. Registrar acceso físico, rol de aplicación y responsables de aprobación.
6. Comprobar nombres distintos contra la lista completa del salón.

El registro debe tener 31 personas distintas. No incluir contraseñas, códigos de MFA ni claves. Si no hay licencia para 31 cuentas, registrar a todo el grupo y acordar las identidades digitales de prueba; no declarar que las demás cuentas fueron creadas.

## Paso 2. Preparar una solicitud

Abrir `Plantillas/solicitudes.csv`. Usar una fila por solicitud y completar:

- Número: SOL-001, SOL-002, etc.
- Tipo: alta, cambio de puesto o baja.
- ID de empleado y correo.
- Fecha efectiva.
- Recursos solicitados y rol.
- Quién aprobó y qué departamento implementa.
- Evidencia y resultado.

Si una solicitud afecta varias áreas, registrar qué acción corresponde a cada una. “Cuenta creada” no demuestra que la tarjeta o aplicación ya funcionen.

## Paso 3. Ejecutar alta del ingeniero

1. Elegir LAB-INGENIERO para el recorrido principal.
2. Registrar puesto Ingeniero de redes A y estado activo.
3. Solicitar a TI cuenta corporativa de prueba.
4. Solicitar acceso digital de mantenimiento a IAM, con aprobación de TI como dueño del servidor.
5. Solicitar tarjeta a Seguridad Física, porque está entre los cuatro autorizados.
6. Confirmar que la aplicación recibió la cuenta por SCIM desde OneLogin. Pedir evidencia de creación automática, no solo una captura del portal.
7. Confirmar registro de MFA con IAM.
8. Pedir pruebas de tarjeta e inicio de sesión y actualizar solicitud como completada.

Resultado: empleado activo, cuenta preparada, tarjeta registrada y mantenimiento permitido.

## Paso 4. Ejecutar cambio de puesto

Usar una cuenta de prueba o hacer esta acción después del recorrido principal.

1. Registrar rol anterior mantenimiento y rol nuevo auditor/consulta.
2. Solicitar retiro del permiso anterior y aprobación del nuevo.
3. IAM cambia el atributo y transmite el cambio a la aplicación.
4. Solicitar una prueba con la sesión que ya estaba abierta: mantenimiento debe ser denegado después de que llegue el cambio.
5. Pedir una nueva prueba de consulta permitida.
6. Revisar con Seguridad Física si cambia el acceso físico. No dar entrada a una quinta identidad.
7. Guardar evidencia de las dos pruebas y cerrar solicitud.

## Paso 5. Ejecutar baja

1. Registrar fecha y hora de baja y marcar el empleado como inactivo.
2. Enviar la solicitud a TI, IAM y Seguridad Física.
3. TI bloquea el inicio de sesión de Microsoft 365 y revoca sesiones según la guía.
4. IAM desactiva al usuario y comprueba el evento de suspensión automática en la aplicación.
5. Seguridad Física retira el UID de autorizados y vuelve a cargar el programa.
6. Pedir pruebas de un nuevo inicio de sesión, acción en una sesión anterior y presentación de la tarjeta.
7. Cerrar la solicitud solo cuando las áreas presenten resultados.

La baja física del ejemplo RFID es manual. La baja digital por SCIM es automática después del cambio en OneLogin. Registrar esa diferencia.

## Paso 6. Mantener seguimiento

Revisar solicitudes abiertas y comprobar que tienen responsable y fecha. Si una está bloqueada por falta de licencia, registrar ese motivo. Una fila aprobada no significa que ya esté implementada.

En el Excel, las tareas combinadas de IAM deben reflejar qué persona hizo cada configuración. Reunir las solicitudes con Auditoría antes del ensayo.

## Carpeta y uso del CSV

```bash
mkdir -p ~/lab-runtime/evidencias/rrhh
```

Abrir los CSV con Excel o Google Sheets y elegir UTF-8 si pregunta por codificación. Conservar los encabezados. Los formularios no envían instrucciones a los sistemas automáticamente: son el registro del procedimiento entre áreas.

## Entregan

Registro de 31 empleados, solicitudes de alta/cambio/baja y evidencia de su cierre. Para el informe, describir quién solicita, quién aprueba, quién implementa y quién verifica.

## Referencias y videos

- [Video oficial OneLogin: ciclo de vida, parte 2](https://www.onelogin.com/resource-center/videos/getting-started-with-identity-lifecycle-management-pt-2): ver creación, cambio y retiro de cuentas.
- [Introducción oficial al aprovisionamiento](https://onelogin.service-now.com/kb?id=kb_article_view&sysparm_article=KB0010298): resultados que RRHH debe pedir a IAM.
- [Microsoft: bloquear acceso de un empleado que sale](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/remove-former-employee-step-1?view=o365-worldwide): resultados que debe pedir a TI.
- [Referencias del paquete](../REFERENCIAS_Y_VIDEOS.md).
