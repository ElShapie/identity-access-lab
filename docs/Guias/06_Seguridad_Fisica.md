# Seguridad Física: RFID, teléfonos y NVR virtual

## Objetivo y responsables

Controlar entrada/salida de cuatro identidades autorizadas y mantener video que permita comprobar los eventos. El NVR virtual está autorizado.

Seguridad Física tiene cinco puestos: coordinación de acceso, montaje del lector, autorización RFID y LED, cámaras y grabación, y operación de entrada y salida.

Laptop 1: lector y registro. Laptop 2: Ubuntu, Docker y Frigate. SOC observa; Seguridad Física administra el NVR. TI apoya red y certificados.

## Parte A. Identificar lector y microcontrolador

Antes de conectar:

1. Fotografiar etiquetas y modelo de lector y placa.
2. Identificar alimentación y forma de conexión: USB, SPI, I2C o serie.
3. Buscar la hoja de datos del fabricante y confirmar tarjetas compatibles.
4. Si el lector es USB que actúa como teclado, comprobar con el profesor cómo se cubrirá el microcontrolador requerido; no aplicar el código MFRC522.
5. Si el lector es PN532, elegir su biblioteca y conexión; no usar el cableado MFRC522.
6. Usar el ejemplo incluido solo cuando se confirme Arduino Uno + MFRC522.

### Ejemplo Arduino Uno y MFRC522

| Lector MFRC522 | Arduino Uno |
|---|---|
| 3.3V | 3.3V |
| GND | GND |
| RST | D9, con adaptación de nivel cuando corresponda |
| SDA/SS | D10, con adaptación de nivel |
| MOSI | D11, con adaptación de nivel |
| MISO | D12, comprobar compatibilidad de entrada |
| SCK | D13, con adaptación de nivel |
| IRQ | Sin conectar en este ejemplo |

El MFRC522 trabaja a 3.3 V y no debe alimentarse con 5 V. Las salidas Uno son de 5 V: comprobar el módulo concreto y usar un adaptador de niveles adecuado para las señales hacia el lector. No asumir que todos los módulos incluyen esa protección. El pin marcado SDA en este modo es selección SPI, no la conexión I2C de un ejemplo distinto.

LED verde: D4 → resistencia apropiada, por ejemplo 330 Ω → LED → GND. LED rojo: D5 con su propia resistencia. Confirmar polaridad y componentes antes de conectar USB.

### Cargar código

1. Instalar Arduino IDE desde su sitio oficial.
2. En administrador de bibliotecas, instalar MFRC522 del proyecto miguelbalboa/rfid.
3. Seleccionar Arduino Uno y puerto correcto.
4. Abrir `Implementacion/rfid/control_acceso.ino` y cargar.
5. Abrir monitor serie a 9600 baudios.
6. Presentar una tarjeta. Inicialmente se niega: el código no contiene UID reales.
7. Copiar el UID sin espacios, en mayúsculas, y relacionarlo con empleado.
8. Reemplazar los cuatro valores pendientes con los UID de LAB-INGENIERO, LAB-ADMIN, LAB-GUARDIA y LAB-AUDITOR.
9. Comprobar que no se repiten UID, cargar de nuevo y probar las cuatro.
10. Probar una tarjeta distinta y verificar LED rojo y rechazo.

El ejemplo compara identificadores para cumplir la práctica. Un UID no demuestra una credencial resistente a copia; describir el alcance del prototipo sin atribuirle protección que no se implementó.

## Parte B. Guardar entradas y salidas

Cerrar monitor serie antes de abrir el registro Python: ambos no deben ocupar el mismo puerto.

En Ubuntu:

```bash
mkdir -p ~/lab-runtime/rfid
cd ~/lab-runtime/rfid
python3 -m venv .venv
source .venv/bin/activate
python -m pip install 'pyserial>=3.5,<4'
python -m serial.tools.list_ports
python registrar_tarjetas.py --puerto /dev/ttyACM0 --archivo eventos_rfid.csv
```

Copiar antes el script desde `Implementacion/rfid/`. Si Ubuntu niega el puerto, TI revisa pertenencia al grupo `dialout`, añade solo al operador autorizado y vuelve a iniciar sesión. No cambiar permisos del puerto para todos.

En Windows, con Python instalado:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install pyserial
.\.venv\Scripts\python.exe -m serial.tools.list_ports
.\.venv\Scripts\python.exe registrar_tarjetas.py --puerto COM3 --archivo eventos_rfid.csv
```

Reemplazar COM3 o `/dev/ttyACM0` por el puerto real. Escribir E y Enter para entrada, S y Enter para salida. La siguiente lectura muestra el modo utilizado. Se guarda hora UTC y local, movimiento, UID, resultado y empleado.

La cámara y el operador comprueban el paso real: una lectura permitida no demuestra por sí sola que la persona cruzó. Sin cerradura electrónica, el operador permite/niega el paso de forma supervisada.

Para revocar una tarjeta, retirar su UID autorizado en el programa, volver a cargar y repetir prueba. La lista máxima tiene cuatro identidades; después de una baja puede tener menos. No autorizar automáticamente a una quinta para ocupar un lugar.

## Parte C. Configurar teléfonos

### Android: cámara de entrada

1. Instalar IP Webcam desde Google Play, paquete `com.pas.webcam`.
2. Conectar a Wi-Fi de laboratorio y a corriente.
3. Permitir cámara. Desactivar grabación de audio si no se utiliza.
4. Seleccionar inicialmente 640 × 480 y alrededor de 5–10 cuadros por segundo.
5. Configurar usuario y contraseña de laboratorio en la app. Usar valores que no contengan caracteres reservados de URL o codificarlos correctamente.
6. Iniciar el servidor y anotar la dirección que realmente muestra.
7. Abrir la página desde una laptop y encontrar el enlace de video MJPEG. Habitualmente es `http://IP:8080/video`; confirmar con la app.
8. Anotar dirección real en inventario y configuración Frigate.
9. Reservar la dirección del teléfono en el router para que no cambie.

### iPhone: cámara interior

1. Instalar IP Camera Lite desde App Store y abrir su modo servidor de cámara IP.
2. Permitir cámara y acceso a red local.
3. Configurar video H.264 y resolución inicial reducida.
4. Configurar credenciales propias; no dejar las predeterminadas.
5. Copiar la URL RTSP completa que entrega la app: puerto y ruta pueden variar.
6. Probarla en VLC mediante Medio → Abrir ubicación de red.
7. Mantener la app en primer plano y el teléfono alimentado; comprobar qué ocurre si se bloquea o cambia de app.
8. Registrar dirección, puerto y ruta. El ejemplo `8554/REEMPLAZAR_RUTA_REAL` no es una ruta garantizada.

La versión Lite puede añadir marca de agua. Comprobar si afecta la evidencia. Si una app no logra un stream compatible y estable, resolverlo antes de confiar en ella para grabar todo el ensayo.

### Probar un stream

TI puede instalar FFmpeg en Ubuntu:

```bash
sudo apt install -y ffmpeg
ffprobe -v error -show_streams 'REEMPLAZAR_URL_REAL_DE_CAMARA'
```

Para RTSP también puede usar `-rtsp_transport tcp` antes de la URL. No publicar el comando con credenciales en la evidencia. Resultado esperado: stream de video identificado y dimensiones reales. Una página web de la cámara no es necesariamente la URL del video.

## Parte D. Instalar Frigate

TI debe haber instalado Docker según su guía. Copiar `Implementacion/nvr/` a `~/lab-runtime/nvr/`.

```bash
cd ~/lab-runtime/nvr
mkdir -p config media certs
cp config.example.yml config/config.yml
cp .env.example .env
chmod 600 .env
```

Editar `.env` con las credenciales de ambas cámaras. En `config/config.yml`, reemplazar direcciones, puerto y ruta reales. Si usan dos Android, duplicar el bloque MJPEG con nombre diferente; si usan dos iPhone, duplicar RTSP. No usar preset HTTP en una URL RTSP.

El archivo activa grabación continua por un día y desactiva detección de objetos. Eso reduce tareas innecesarias, pero el video aún requiere procesamiento. MJPEG se convierte para grabarlo y puede consumir más CPU que RTSP/H.264. Reducir resolución/cuadros si el equipo se satura.

### Certificado local para el NVR

El NVR usa HTTPS con autenticación. TI prepara un certificado válido para su dirección de laboratorio y distribuye únicamente la autoridad pública a los dispositivos que lo consultarán.

En la laptop NVR:

```bash
sudo apt install -y mkcert libnss3-tools
mkcert -install
mkcert -cert-file certs/fullchain.pem -key-file certs/privkey.pem 10.31.0.20 localhost 127.0.0.1
mkcert -CAROOT
```

El último comando muestra la carpeta con `rootCA.pem`. Copiar solo ese archivo a los clientes y verificar con TI que corresponde al certificado del laboratorio. No compartir `rootCA-key.pem` ni `privkey.pem`.

- Ubuntu cliente: instalar el certificado público en el almacén de confianza con apoyo de TI y reiniciar navegador.
- Windows cliente: importar el certificado público como autoridad de confianza del laboratorio, con permiso del propietario del equipo.
- iPhone: instalar perfil del certificado y habilitar su confianza en Ajustes, según la guía mkcert/Apple.
- Android: instalar certificado de autoridad en Seguridad/Cifrado y credenciales, según versión; confirmar que el navegador utilizado lo reconoce.

Si hay advertencia de certificado, corregir dirección o confianza con TI. No indicar a los usuarios que ignoren la advertencia. Retirar la autoridad de laboratorio de los equipos personales al cerrar el proyecto si ya no se necesita.

### Iniciar grabador

En `compose.yml`, reemplazar `10.31.0.20` si el NVR tiene otra dirección. Esa dirección debe existir en la laptop o máquina virtual que ejecuta Docker.

```bash
sudo docker compose config --quiet
sudo docker compose pull
sudo docker compose up -d
sudo docker compose ps
sudo docker compose logs --tail=100 frigate
```

Abrir `https://10.31.0.20:8971` desde un cliente preparado. La contraseña inicial del administrador aparece en los logs del primer arranque. Cambiarla desde Settings → Users y crear usuarios de consulta para SOC. No entregar a todo el grupo credenciales de administrador.

Frigate permanece en la red local. No publicar su puerto interno 5000 ni dirigir el túnel de la aplicación al NVR.

Si el validador de Frigate rechaza una clave, comprobar la versión instalada y su esquema antes de cambiar configuración. No sustituir el archivo por un YAML de un video antiguo.

## Parte E. Probar grabación y almacenamiento

1. Ver ambas cámaras en Live.
2. Dejar grabar diez minutos, incluyendo un periodo sin movimiento.
3. Abrir History, elegir cada cámara y reproducir inicio, mitad y final de la prueba.
4. Exportar un intervalo donde se vea el acceso autorizado y otro con rechazo.
5. Abrir los MP4 exportados en otra laptop.
6. Comprobar espacio real:

```bash
df -h .
du -sh media
sudo docker stats --no-stream identity-access-lab-nvr
```

Estimar consumo diario a partir de una muestra real. Ejemplo propuesto: dos streams de 2 Mb/s suman unos 43.2 GB al día antes de otros archivos. La cifra cambia con cámaras y conversión; no reservar espacio basándose solo en ese ejemplo.

Para demostrar 24/7, dejar grabar 24 horas si el calendario lo permite, mantener energía y evitar suspensión/cierre de tapa. SOC registra cortes. Si solo probaron una hora, declarar una hora y configuración continua; no declarar 24 horas sin evidencia. Con retención de un día, exportar evidencias antes de que salgan de la ventana. Aumentar retención solo si hay espacio suficiente.

## Parte F. Móvil y continuidad

1. Abrir la dirección HTTPS del NVR en el navegador del teléfono de monitoreo.
2. Iniciar sesión con usuario de consulta y verificar Live e History.
3. Probar el acceso desde la misma red y registrar ese alcance. Para otra red se requiere un diseño de acceso remoto adicional; no basta cambiar el teléfono a datos móviles.
4. Reiniciar el contenedor durante una prueba controlada y comprobar retorno del servicio y persistencia de videos.
5. Guardar configuración sin secretos y copia del circuito/código.

```bash
sudo docker compose restart frigate
sudo docker compose logs --tail=50 frigate
```

Resultado esperado: vuelve a grabar y conserva archivos previos. Registrar el corte provocado, no ocultarlo en la prueba de continuidad.

## Entregan

Modelo real de placa/lector, circuito, código adaptado, cuatro UID registrados, CSV, ubicaciones de cámaras, configuración Frigate, exportaciones, duración probada, espacio y monitoreo móvil. No incluir secretos ni claves de certificados.

## Referencias y videos

- [Frigate: instalación](https://docs.frigate.video/frigate/installation/).
- [Frigate: grabación continua](https://docs.frigate.video/configuration/record/).
- [Frigate: presets MJPEG y RTSP](https://docs.frigate.video/configuration/ffmpeg_presets/).
- [Frigate: autenticación](https://docs.frigate.video/configuration/authentication/) y [certificados](https://docs.frigate.video/configuration/tls/).
- [Android IP Webcam](https://play.google.com/store/apps/details?id=com.pas.webcam) y [iPhone IP Camera Lite](https://apps.apple.com/us/app/ip-camera-lite/id1013455241).
- [Biblioteca RFID y modelos compatibles](https://github.com/miguelbalboa/rfid).
- [Certificados de laboratorio mkcert](https://github.com/FiloSottile/mkcert).
- [Video: Frigate con Docker](https://www.youtube.com/watch?v=KMD72_Wfp3E): apoyo visual; no necesitan su parte de IA, MQTT ni Home Assistant.
- [Video: Arduino y MFRC522](https://www.youtube.com/watch?v=CQLPo7xqORQ): solo si coincide el hardware; revisar alimentación y niveles contra el módulo real.
