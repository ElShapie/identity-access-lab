# Identity Access Lab

Laboratorio de control de acceso físico y digital, con documentación en español para 31 puestos organizados en siete departamentos. El repositorio contiene instrucciones y ejemplos; las plataformas todavía requieren configuración y pruebas en el entorno de quien los utilice.

**Contenido público sin personas identificadas.** Los puestos, cuentas de ejemplo y direcciones de red son genéricos. Las plantillas CSV están vacías. Los nombres, la institución, las asignaciones personales, las tarjetas reales, las contraseñas y las evidencias operativas se mantienen fuera de este repositorio.

## Empezar aquí

1. Leer el [manual general](docs/LEER_PRIMERO.md), también disponible en [PDF](docs/LEER_PRIMERO.pdf).
2. Leer la guía correspondiente al departamento en la tabla siguiente.
3. Revisar los [diagramas](docs/Diagramas/Diagramas_completos.pdf).
4. TI prepara red y aplicación; Seguridad Física prepara lector y NVR; IAM conecta OneLogin.
5. SOC revisa eventos y Auditoría comprueba el recorrido completo.

| Departamento | Puestos | Guía editable | PDF |
|---|---:|---|---|
| Dirección | 3 | [Guía](docs/Guias/01_Direccion.md) | [PDF](docs/Guias/01_Direccion.pdf) |
| RRHH | 3 | [Guía](docs/Guias/02_RRHH.md) | [PDF](docs/Guias/02_RRHH.pdf) |
| TI | 7 | [Guía](docs/Guias/03_TI.md) | [PDF](docs/Guias/03_TI.pdf) |
| IAM / OneLogin | 5 | [Guía](docs/Guias/04_IAM_OneLogin.md) | [PDF](docs/Guias/04_IAM_OneLogin.pdf) |
| SOC | 5 | [Guía](docs/Guias/05_SOC.md) | [PDF](docs/Guias/05_SOC.pdf) |
| Seguridad Física | 5 | [Guía](docs/Guias/06_Seguridad_Fisica.md) | [PDF](docs/Guias/06_Seguridad_Fisica.pdf) |
| Auditoría | 3 | [Guía](docs/Guias/07_Auditoria.md) | [PDF](docs/Guias/07_Auditoria.pdf) |

La [guía de Python](docs/Guias/08_Uso_de_Python.md), también en [PDF](docs/Guias/08_Uso_de_Python.pdf), explica los comandos para los cuatro archivos `.py`, en qué equipo se usan y cómo resolver problemas frecuentes.

## Qué implementa cada sistema

| Sistema | Uso |
|---|---|
| RFID y microcontrolador | Lectura de tarjeta, cuatro identidades de prueba, LED permitido/denegado y salida serie |
| Registrador Python | CSV privado con lecturas y hora de recepción |
| Frigate 0.17.1 | NVR de código abierto, grabación continua y consulta local de cámaras |
| Android / iPhone | Cámaras IP mediante las aplicaciones indicadas en la guía |
| OneLogin | Inicio de sesión OIDC, MFA y aprovisionamiento SCIM de la aplicación |
| Aplicación Flask | Validación de cuenta activa y permisos para consulta, mantenimiento, administración y registros |
| Microsoft 365 / Entra | Ejercicios de cuentas, licencias, contraseña, MFA y auditoría |

OneLogin es obligatorio en este diseño. Microsoft 365 y OneLogin se administran por separado: no se presenta una sincronización o federación entre ellos. El hub SOC relaciona registros y video mediante hora e identidad; no existe un panel que correlacione automáticamente todas las fuentes.

## Recursos y dependencias

- Dos laptops designadas por departamento; Ubuntu 24.04 para servidor y NVR, físico o en máquina virtual con conectividad comprobada.
- Uno o dos switches, router/punto de acceso, cables y alimentación.
- Dos teléfonos, uno Android y uno iPhone, o adaptar la configuración a los disponibles.
- Lector y microcontrolador por identificar. El ejemplo de cableado/código corresponde exclusivamente a Arduino Uno y MFRC522.
- Tenant OneLogin con los conectores y permisos necesarios; entorno Microsoft 365 con licencias y acceso administrativo disponibles.

Las direcciones `10.31.0.0/24` son una red ficticia de ejemplo. Confirmar la red real antes de usar los archivos de configuración. Las cuentas `LAB-INGENIERO`, `LAB-ADMIN`, `LAB-GUARDIA` y `LAB-AUDITOR` representan perfiles de demostración, no integrantes reales.

## Descargar y consultar

En GitHub, usar **Code → Download ZIP**, descomprimir y abrir los PDF. Para leer no hace falta Python, Docker ni LaTeX. Los PDF tienen Times New Roman incrustada y están en blanco y negro.

Para trabajar con Git:

```bash
git clone https://github.com/ElShapie/identity-access-lab.git
cd identity-access-lab
```

## Comprobar el código sin arrancar plataformas

Desde la raíz del repositorio:

```bash
python3 -m unittest discover -s Implementacion/app -p 'test_store.py' -v
python3 -m pip install -r scripts/requirements-check.txt
python3 scripts/check_public_content.py
```

Las siete pruebas verifican el almacenamiento y permisos locales. No prueban los tenants, las cámaras ni el lector. El segundo comando instala una dependencia para revisar PDF; conviene ejecutarlo dentro de un entorno virtual.

Para arrancar servicios y el registrador, seguir la guía de Python. Copiar los componentes necesarios a `~/lab-runtime/`, fuera del clon público; los datos operativos permanecen allí. `store.py` es un módulo utilizado por la aplicación. `app.py` se sirve mediante Gunicorn; no se arranca con `python app.py`.

## Estructura

```text
docs/                  Guías Markdown, fuentes LaTeX y PDF públicos
docs/Guias/            Guías por departamento y uso de Python
docs/Diagramas/        SVG genéricos, fuentes LaTeX y PDF de diagramas
Implementacion/app/    Aplicación OIDC/SCIM, permisos y pruebas
Implementacion/nvr/    Configuración de ejemplo de Frigate
Implementacion/rfid/   Programa Arduino y registrador Python
Plantillas/            Formularios CSV vacíos
scripts/               Revisión de contenido y compilación LaTeX
.github/               Comprobaciones automáticas y plantillas de colaboración
```

Consultar [referencias y videos](docs/REFERENCIAS_Y_VIDEOS.md), [cómo contribuir](CONTRIBUTING.md), [reglas de privacidad](PRIVACIDAD.md) y [edición de PDF/LaTeX](docs/COMPILAR_LATEX.md).

## Estado de validación

La documentación y los ejemplos se revisaron antes de publicar. Las pruebas locales de permisos pasan. La integración OneLogin, el video continuo y el hardware deben comprobarse con las cuentas y equipos del laboratorio. No guardar los resultados con personas identificadas en GitHub, incluidos Issues, comentarios o pull requests.
