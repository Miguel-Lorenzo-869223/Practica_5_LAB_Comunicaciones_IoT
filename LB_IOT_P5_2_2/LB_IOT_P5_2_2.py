# ------------------------------------------------------------
#  Author: Miguel A.Lorenzo
#  Date: 17/09/2026
#  Subject: IoT Communications Laboratory
#  Master: MSc in Electronic Engineering
#  University: University of Zaragoza EINA/UNIZAR
# ------------------------------------------------------------


import serial
import time

PORT = "COM5"        # Arduino serial port
BAUD = 115200        # Must match Serial.begin() in Arduino

def open_serial():
    """Attempts to establish a serial connection continuously until successful."""
    while True:
        try:
            # Check if there is data available in the incoming buffer
            print(f"Connecting to {PORT}...")
            ser = serial.Serial(PORT, BAUD, timeout=1)
            print("Serial port connected...\n")
            return ser
        except serial.SerialException:
            print("Failed to open port. Retrying...")
            time.sleep(1)

def main():
    ser = open_serial()

    while True:
        try:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8', errors='ignore').strip()
                print(line)
        except serial.SerialException:
            print("Connection lost...")
            ser = open_serial()
        except KeyboardInterrupt:
            print("\nClosing Serial...")
            ser.close()
            break

if __name__ == "__main__":
    main()
