"""Guarda lecturas RFID con hora UTC y local; E/S cambia el modo explícitamente."""
import argparse
import csv
import threading
from datetime import datetime, timezone
from pathlib import Path
import serial

parser = argparse.ArgumentParser()
parser.add_argument('--puerto', required=True, help='Ejemplo: COM3 o /dev/ttyACM0')
parser.add_argument('--archivo', default='eventos_rfid.csv')
args = parser.parse_args()
port = serial.Serial(args.puerto, 9600, timeout=1)
path = Path(args.archivo)
new_file = not path.exists() or path.stat().st_size == 0

def commands():
    while True:
        try:
            command = input('E=entrada, S=salida: ').strip().upper()
            if command in ('E', 'S'):
                port.write(command.encode('ascii'))
                print('Modo solicitado:', 'ENTRADA' if command == 'E' else 'SALIDA')
        except EOFError:
            return

threading.Thread(target=commands, daemon=True).start()
try:
    with path.open('a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if new_file:
            writer.writerow(['hora_utc','hora_local','movimiento','uid','resultado','empleado'])
        while True:
            line = port.readline().decode('utf-8', errors='replace').strip()
            if not line:
                continue
            print(line)
            parts = line.split(',')
            if len(parts) != 4 or parts[0] not in ('ENTRADA', 'SALIDA') or parts[2] not in ('PERMITIDO','DENEGADO'):
                continue
            now = datetime.now(timezone.utc)
            writer.writerow([now.isoformat(), now.astimezone().isoformat(), *parts])
            f.flush()
except KeyboardInterrupt:
    print('\nRegistro terminado.')
finally:
    port.close()
