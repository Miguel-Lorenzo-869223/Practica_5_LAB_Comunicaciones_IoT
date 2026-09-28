# ------------------------------------------------------------
#  Author: Miguel A.Lorenzo
#  Date: 17/09/2026
#  Subject: IoT Communications Laboratory
#  Master: MSc in Electronic Engineering
#  University: University of Zaragoza EINA/UNIZAR
# ------------------------------------------------------------

import serial
import time
import numpy as np

PORT = "COM5"  # Revisa tu puerto
BAUD = 115200

try:
    ser = serial.Serial(PORT, BAUD, timeout=1)
    time.sleep(2)
    ser.reset_input_buffer()
    print(f"✔ Conectado a {PORT}. Leyendo datos...\n")
except Exception as e:
    print(f"❌ Error al abrir el puerto: {e}")
    exit()

window_acc = []
last_stats_time = time.time()

try:
    while True:
        # Lee directamente la línea
        raw_line = ser.readline().decode('utf-8', errors='ignore').strip()

        if raw_line:
            parts = raw_line.split(';')

            if len(parts) >= 3:
                try:
                    ax = float(parts[0])
                    ay = float(parts[1])
                    az = float(parts[2])

                    print(f"Acc X: {ax:6.3f} | Acc Y: {ay:6.3f} | Acc Z: {az:6.3f}")
                    window_acc.append([ax, ay, az])

                except ValueError:
                    pass

        # Cálculo de estadísticas cada 5 segundos
        if time.time() - last_stats_time >= 5.0:
            if len(window_acc) > 0:
                acc_arr = np.array(window_acc)
                mean_acc = np.mean(acc_arr, axis=0)
                std_acc = np.std(acc_arr, axis=0)

                print("\n" + "=" * 55)
                print(f"📊 ESTADÍSTICAS 5s ({len(window_acc)} muestras)")
                print(f"MEDIA   (X, Y, Z): {mean_acc[0]:.3f}, {mean_acc[1]:.3f}, {mean_acc[2]:.3f}")
                print(f"DESV.ST (X, Y, Z): {std_acc[0]:.3f}, {std_acc[1]:.3f}, {std_acc[2]:.3f}")
                print("=" * 55 + "\n")

            window_acc.clear()
            last_stats_time = time.time()

except KeyboardInterrupt:
    print("\nPrograma detenido.")

finally:
    ser.close()
    print("Puerto cerrado.")