# Diligencias operativas por área

Esta versión se puede compartir con responsables y trabajadores. Usa únicamente identificadores `EMP`; los nombres se consultan en el panel privado. No escriba nombres, correos, contraseñas, UID completos de tarjetas ni direcciones públicas en repositorios, capturas o entregables.

## Regla de trabajo

1. El responsable abre el panel de su área y revisa tareas, fechas, bloqueos y cooperación.
2. Cada trabajador localiza su `EMP`, ejecuta su actividad y carga una evidencia entendible.
3. El responsable comprueba el archivo, describe el resultado y lo envía al Centro de control DPO.
4. DPO aprueba o devuelve la evidencia con una corrección concreta. Solo una aprobación cuenta como avance.
5. Los incidentes se registran por separado y se escalan por la ruta indicada.

## Dirección (Apoyo transversal)

Reportan primero a `EMP-003` para avance y calendario. Riesgos de seguridad se envían a `EMP-002`; decisiones generales a `EMP-001`.

- `EMP-001`: aprobar alcance, resolver decisiones y, como técnico de TI, entregar plano, etiquetado y pruebas del cableado estructurado.
- `EMP-002`: mantener política de acceso, criterios de severidad y coordinación de incidentes.
- `EMP-003`: calendario, dependencias, reuniones, ensayos y guion integrado.

Entrega del área: registro de decisiones, calendario, política, guion y acta de cierre.

## TI (Access Control / Monitoring)

Reportan primero a `EMP-010`. RFID y cámaras se coordinan con `EMP-024`; identidades y permisos con `EMP-014`.

- `EMP-010`: responsable de TI; topología, inventario de puertos, aprobación de cambios y coordinación de VM.
- `EMP-001`: cableado estructurado; plano físico, etiquetas en ambos extremos, tabla switch-puerto-VLAN y pruebas de conectividad.
- `EMP-009`: configuración de red, VLAN, enlaces y mantenimiento durante el recorrido.
- `EMP-008`: segunda revisión de topología, pruebas permitidas/denegadas y plan de infraestructura.
- `EMP-011`: VM-HUB, interfaz, HTTPS, servicio, respaldo y recuperación.
- `EMP-013`: soporte, pruebas de equipos, MFA y recolección técnica de evidencias.
- `EMP-007`: inventario técnico de equipos, cuentas de práctica y asignaciones.

Entrega del área: topología, tabla de cableado/VLAN, VM operativas, matriz de permisos, registro de pruebas y restauración de respaldo.

## SOC (Monitoring)

Reportan primero a `EMP-019`. Eventos físicos se coordinan con `EMP-024`; incidentes relevantes se escalan a `EMP-002`.

- `EMP-019`: turnos, procedimiento de monitoreo y coordinación de incidentes.
- `EMP-020`: cámara de entrada y correlación con eventos RFID.
- `EMP-021`: cámara interior, acceso móvil y continuidad de imagen.
- `EMP-022`: correlación de registros por EMP, hora y fuente.
- `EMP-023`: alta, seguimiento, contención, cierre y lección aprendida del incidente de prueba.

Entrega del área: puesto de monitoreo, bitácora, incidente completo, reporte y prueba de que SOC no puede administrar permisos.

## Seguridad Física (Access Control / Monitoring)

Reportan primero a `EMP-024`. Fallas técnicas van a `EMP-010`, permisos de identidad a `EMP-014` y alertas a `EMP-019`.

- `EMP-024`: lista de acceso físico, aprobaciones y control de cambios.
- `EMP-026`: autorización RFID, indicador visual y registro de permitido/denegado.
- `EMP-027`: teléfonos como cámaras IP, NVR virtual, grabación y recuperación por hora.
- `EMP-028`: operación de entrada/salida y validación de eventos.
- `EMP-032`: identificación y conexión segura del lector y microcontrolador; lectura de tarjeta sin publicar UID completo.
- `EMP-033`: enlace con SOC y correlación de cámara, tarjeta y alerta.

Entrega del área: esquema RFID, registro de tarjetas por EMP, lista vigente, eventos de entrada/salida y video recuperable.

## RRHH (Identity and Access Management)

Reportan primero a `EMP-004`. Altas, cambios y bajas aprobados se envían a `EMP-014`; Auditoría recibe la trazabilidad.

- `EMP-004`: validar identidad mínima, puesto, estado y solicitud.
- `EMP-005`: preparar alta y comprobar incorporación.
- `EMP-006`: tramitar cambio y baja, incluidos retiro de permisos y tarjeta.
- `EMP-034`: mantener registro y constancias de movimientos sin exponer nombres en documentos compartidos.

Entrega del área: registro por EMP, solicitudes de alta/cambio/baja y bitácora de recepción y ejecución.

## IAM (Identity Management / Identity and Access Management)

Reportan primero a `EMP-014`. Eventos sospechosos van a `EMP-019`; movimientos se validan con RRHH y las pruebas se entregan a Auditoría.

- `EMP-014`: matriz de mínimo privilegio, aprobaciones y coordinación de solicitudes.
- `EMP-015`: OneLogin, grupos, roles y pruebas permitidas/denegadas.
- `EMP-016`: ciclo de vida; alta, cambio, retiro de permisos y baja.
- `EMP-017`: MFA, recuperación autorizada y evidencia del desafío real.
- `EMP-018`: aprovisionamiento y documentación de solicitudes, resultados y tiempos.
- `EMP-012`: Microsoft 365; cuentas, roles mínimos, licencias disponibles, recuperación y registros.

Entrega del área: matriz de roles, configuración de OneLogin, MFA, prueba negativa y ciclo de vida completo.

## Auditoría (Identity Management / Identity and Access Management)

Reportan primero a `EMP-031`. Hallazgos se devuelven al responsable revisado; riesgos críticos se escalan a `EMP-002`.

- `EMP-029`: auditar RFID, accesos físicos, cámaras, NVR y montaje.
- `EMP-030`: auditar cuentas, roles, MFA, OneLogin, Microsoft 365 y bajas.
- `EMP-031`: matriz requisito-prueba-evidencia, informe, presentación e índice de archivos.

Entrega del área: matriz de pruebas, índice de evidencias, hallazgos, informe y acta de auditoría.

## Cómo debe ser una evidencia

Debe indicar el `EMP`, área, actividad, fecha, equipo de laboratorio, pasos ejecutados, resultado esperado, resultado obtenido y archivo asociado. Oculte secretos y datos personales. Una captura aislada no demuestra una prueba; incluya contexto y, cuando corresponda, un caso permitido y otro denegado.

## Uso de los cuadernos PDF

En `docs/Controles_Area/` existe un cuaderno por área. El responsable lo usa para planificar, registrar bloqueos, dirigir pruebas y cerrar entregables. Los trabajadores consultan la sección de puestos y la guía paso a paso para conocer su actividad. Las casillas y firmas son para la copia local; no suba copias rellenadas al repositorio público.
