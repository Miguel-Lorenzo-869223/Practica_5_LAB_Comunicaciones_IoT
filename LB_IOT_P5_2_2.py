import serial
import time

PORT = "COM7"        # Cambia esto al puerto de tu Arduino
BAUD = 115200        # Debe coincidir con Serial.begin()

def open_serial():
    while True:
        try:
            print(f"Conectando a {PORT}...")
            ser = serial.Serial(PORT, BAUD, timeout=1)
            print("✔ Puerto serie conectado\n")
            return ser
        except serial.SerialException:
            print("❌ No se pudo abrir el puerto. Reintentando...")
            time.sleep(1)

def main():
    ser = open_serial()

    while True:
        try:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8', errors='ignore').strip()
                print(line)
        except serial.SerialException:
            print("⚠ Conexión perdida. Reconectando...")
            ser = open_serial()
        except KeyboardInterrupt:
            print("\nPrograma terminado por el usuario.")
            ser.close()
            break

if __name__ == "__main__":
    main()
