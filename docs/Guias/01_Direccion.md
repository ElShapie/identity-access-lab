# Dirección y Gestión del Proyecto

## Objetivo y responsabilidades

Organizar el trabajo, aprobar reglas del escenario y comprobar que los departamentos entreguen un sistema integrado. Dirección no tiene acceso automático al área restringida ni recibe permisos de administración por su cargo.

Puestos: dirección general, responsable de seguridad y coordinación. Cada puesto debe tener una persona asignada en el control privado. Estos cargos no conceden permisos técnicos por sí mismos.

## Paso 1. Asignar puestos sin publicar datos personales

1. Revisar los 31 puestos genéricos de los diagramas.
2. Asignar una persona a cada puesto en un registro privado separado del repositorio.
3. Mantener en privado nombres, correos, tarjetas, aprobadores y contactos.
4. Confirmar que no hay tareas sin responsable ni conteos duplicados.
5. Actualizar los departamentos y funciones genéricas si cambia el diseño.
6. Acordar responsables y suplentes por área en el control privado.

Resultado: 31 puestos con tareas definidas y documentación pública sin datos personales.

## Paso 2. Registrar decisiones de implementación

Completar `Plantillas/acuerdos.csv` con fecha, decisión, responsable y evidencia. Registrar NVR virtual autorizado, alcance del monitoreo móvil, sustitución de transceptores, recursos de Microsoft 365/OneLogin y formato del informe.

OneLogin es obligatorio: si el entorno no permite un conector o aprovisionamiento, solicitar a la institución acceso o licencia que lo permita. No aprobar una sustitución por otra plataforma.

## Paso 3. Asignar equipos

1. Confirmar las 14 laptops principales del archivo inicial.
2. Registrar propietario, función, cargador y ubicación.
3. Seleccionar servidor TI y grabador de Seguridad Física. Identificar su sistema operativo y si se preparará Ubuntu en una máquina virtual.
4. Reservar dos teléfonos con sus cargadores y soportes.
5. Confirmar switches, router/punto de acceso, cables y adaptadores.
6. Asignar fecha para identificar físicamente lector y microcontrolador.

Resultado: el inventario indica qué existe y quién lo lleva. “Posiblemente disponible” sigue siendo un pendiente.

## Paso 4. Crear calendario por resultados

| Etapa | Resultado exigido para cerrar |
|---|---|
| Preparación | Personal, recursos y acceso a plataformas confirmados |
| Infraestructura | Red, aplicación básica y un teléfono accesible |
| Control físico | UID, cuatro tarjetas, LED y CSV funcionando |
| Identidades | OneLogin real, roles, MFA, creación y baja automática |
| Monitoreo | Dos cámaras, móvil, grabación y recuperación de video |
| Integración | Entrada, tarea permitida, tarea denegada, salida y baja |
| Entrega | Pruebas, informe en inglés, presentación y resultados |

Poner fechas reales en el Excel. Una etapa puede continuar mientras otra espera recursos, pero no declarar completa una dependencia que falla.

## Paso 5. Aprobar reglas del escenario

1. Confirmar las cuatro identidades físicas: LAB-INGENIERO, LAB-ADMIN, LAB-GUARDIA y LAB-AUDITOR.
2. Aprobar funciones digitales: mantenimiento para ingeniero, administración para administrador, consulta/registros para auditor y funciones específicas para Seguridad Física.
3. Establecer que RRHH solicita, el dueño del recurso aprueba y TI/IAM/Seguridad Física configuran.
4. Prohibir la aprobación de un permiso por la misma persona que lo solicita cuando puedan separar funciones.
5. Registrar qué ocurre con una tarjeta desconocida, una baja y un fallo de cámara.

## Paso 6. Revisión de progreso

En cada reunión, preguntar por resultado, evidencia, dificultad y siguiente acción. Actualizar estado y porcentaje en el Excel. Si se declara “Terminado”, abrir su evidencia y comprobarla.

Ejemplos de dificultades útiles: “La aplicación recibe un rechazo de callback”; “OneLogin deja el alta en pendiente”; “El iPhone cambia de dirección”. Evitar registros como “no funciona” sin indicar el paso fallido.

## Paso 7. Coordinar ensayo y exposición

1. Comprobar que RRHH dio de alta al ingeniero antes del recorrido.
2. TI, IAM y Seguridad Física verifican el estado inicial.
3. SOC abre imágenes y registros.
4. Mostrar visitante rechazado, ingeniero autorizado, MFA, mantenimiento, auditor rechazado en mantenimiento y salida.
5. Hacer cambio de rol y baja al final para no romper los pasos anteriores.
6. Auditoría presenta resultados reales y limitaciones.
7. Medir duración y ajustar al tiempo del profesor.

Guardar una copia de videos y registros por si falla internet en vivo. Esas evidencias corresponden a un ensayo identificado; no simular que ocurrieron en ese momento.

## Comandos y archivos

Dirección trabaja principalmente en el control compartido. Para crear carpetas en una laptop Ubuntu:

```bash
mkdir -p ~/lab-runtime/evidencias/direccion
mkdir -p ~/lab-runtime/entrega
```

En Windows, crear las mismas carpetas con el explorador. No necesitan instalar Docker ni ejecutar comandos administrativos para coordinar el grupo.

## Entregan

Lista revisada, decisiones, inventario, calendario, política de acceso, guion y carpeta de entrega. Cada documento indica fecha y responsable.

## Referencias y videos

- [Video oficial OneLogin: grupos, roles y asignación automática](https://www.onelogin.com/video/groups-roles-and-mappings-oh-my): comprender qué debe pedir Dirección a IAM.
- [Video oficial OneLogin: ciclo de vida de identidades, parte 2](https://www.onelogin.com/resource-center/videos/getting-started-with-identity-lifecycle-management-pt-2): identificar resultados de altas y bajas.
- [Introducción oficial al aprovisionamiento](https://onelogin.service-now.com/kb?id=kb_article_view&sysparm_article=KB0010298): diferencia entre asignar una aplicación y mantener su cuenta sincronizada.
- [Referencia del proyecto](../REFERENCIAS_Y_VIDEOS.md): fuentes y materiales compartidos.
