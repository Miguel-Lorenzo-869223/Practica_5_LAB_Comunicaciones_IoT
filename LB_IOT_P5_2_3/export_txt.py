# ------------------------------------------------------------
#  Author: Miguel A.Lorenzo
#  Date: 17/09/2026
#  Subject: IoT Communications Laboratory
#  Master: MSc in Electronic Engineering
#  University: University of Zaragoza EINA/UNIZAR
# ------------------------------------------------------------
"""
===============================================================================
Serial Data Logger to TXT
===============================================================================
Reads incoming serial data from Arduino and appends each line into a .txt file.
Data fields are delimited by semicolons (;) with a newline (\n) at the end of
each sample for direct opening/importing in Microsoft Excel.
===============================================================================
"""

import serial
import time

# --- CONFIGURATION ---
PORT = "COM5"        # Arduino serial port (Update to match Device Manager)
BAUD = 115200        # Baud rate (Must match Serial.begin() in Arduino)
FILE_NAME = "read_ble_nano_33.txt"


def open_serial():
    """Attempts to establish a serial connection continuously until successful."""
    while True:
        try:
            print(f"Connecting to {PORT}...")
            ser = serial.Serial(PORT, BAUD, timeout=1)
            print("Serial port connected\n")
            return ser
        except serial.SerialException:
            print("Failed to open port. Retrying in 1 second...")
            time.sleep(1)


def main():
    # Establish serial connection
    ser = open_serial()

    # Open text file in append mode ('a') to retain previous measurements
    with open(FILE_NAME, mode='a', encoding='utf-8') as file:
        print(f"📄 Logging data to '{FILE_NAME}'... Press Ctrl+C to stop.\n")

        while True:
            try:
                # Check if new bytes are waiting in the input buffer
                if ser.in_waiting > 0:
                    raw_line = ser.readline().decode('utf-8', errors='ignore').strip()

                    if raw_line:
                        # Replace spaces or commas with semicolons (;) for Excel columns
                        formatted_line = raw_line.replace(",", ";").replace(" ", ";")

                        # Append newline (\n) at the end of each sample
                        file_entry = f"{formatted_line}\n"

                        # Write to file and flush buffer immediately to disk
                        file.write(file_entry)
                        file.flush()

                        print(f"Logged: {formatted_line}")
                else:
                    time.sleep(0.01)  # Prevent high CPU usage while waiting

            except serial.SerialException:
                print("Connection lost. Reconnecting...")
                ser = open_serial()

            except KeyboardInterrupt:
                print("\nProgram terminated by user.")
                ser.close()
                break


if __name__ == "__main__":
    main()