# Practica_5_LAB_Comunicaciones_IoT

# Practical Exercise 2: Communication, Management, and Visual Representation of Sensor Data with Python

> **IoT Communications Laboratory**  
> MSc in Electronic Engineering — University of Zaragoza (EINA/UNIZAR)  
> **Author:** Miguel A. Lorenzo  
> **Date:** October 2026  

---

## 📌 Project Overview

This repository contains the complete software implementation for **Practical Exercise 2** of the IoT Communications Laboratory. The primary objective is to acquire, process, log, and visualize real-time inertial sensor telemetry transmitted over a serial link from an **Arduino Nano** microcontroller using **Python**.

Building upon Section 5 of Practical Exercise 1—where 3-axis IMU acceleration data is sampled over I2C and forwarded via UART at regular intervals—this project covers the end-to-end data pipeline on the host PC:
1. **Serial Data Reception:** Reading raw CSV-formatted telemetry streams over UART/USB.
2. **File Persistence:** Structuring incoming readings into delimited text/CSV log files formatted for spreadsheet tools like Microsoft Excel.
3. **Statistical Windowing:** Calculating 5-second rolling window metrics (Mean $\mu$ and Standard Deviation $\sigma$) across all active sensor axes.
4. **Real-Time Visualization:** Rendering dynamic data plots using Matplotlib and thread-safe animation mechanisms without UI thread blocking.

---

## 🛠️ Hardware Setup & Key Peripherals

- **Arduino Nano Board:**
  - **Inertial Measurement Unit (IMU):** Onboard ST LSM9DS1 9-DOF sensor (3-axis Accelerometer, 3-axis Gyroscope, 3-axis Magnetometer) queried via internal I2C/SPI bus.
  - **UART Serial Interface:** Configured at **115200 baud**, streaming semicolon-delimited (`;`) float vectors terminated with a newline (`\n`).
- **Host PC Development Platform:**
  - **USB Interface:** Virtual COM port communication layer.

---

## 📱 Required Applications & Software Environment

- **Embedded Firmware Environment:**
  - **Development IDE:** Arduino IDE (v2.x or later).
  - **Core Board Package:** `Arduino Mbed OS Nano Boards` (for Arduino Nano 33 BLE / Nano family).
  - **Required C++ Libraries:** `Arduino_LSM9DS1` (or equivalent onboard IMU driver).
- **Host Workstation / Python Environment:**
  - **Python Runtime:** Python 3.9+ (64-bit recommended).
  - **Diagnostic Tools:** [Termite Serial Terminal](https://www.compuphase.com/software_termite.htm) or PuTTY.
  - **Required Python Packages:**
    - `pyserial`: Serial port abstraction and hardware interface driver.
    - `numpy`: High-performance array manipulation and statistical computations.
    - `matplotlib`: Data plotting framework and animation tools.
  - **Data Analysis Software:** Microsoft Excel or LibreOffice Calc for CSV log verification.

---

## 🏗️ Exercises & System Architectures

### 1. Exercise 2.1 — Hardware Telemetry & Serial Monitor Verification
- **Platform:** Arduino Nano & Termite Serial Terminal
- **Description:** Verifies that the Arduino Nano firmware initializes the LSM9DS1 IMU and continuously streams raw 9-DOF readings over UART at 115200 baud.
- **Key Features:** Confirms data integrity and frame syntax (e.g., `ax;ay;az;gx;gy;gz;mx;my;mz`) via standalone serial diagnostic utilities (Termite) prior to running custom Python backend scripts.

### 2. Exercise 2.2 — Python Real-Time Serial Reader
- **Platform:** Python (`pyserial`)
- **Description:** Implements a baseline Python console application that opens the target serial port (`COMx` or `/dev/ttyACM0`) and streams raw sensor data to standard output.
- **Key Features:** Serial port initialization with connection timeout safeguards, error handling for corrupted frames, and real-time terminal logging matching hardware outputs.

### 3. Exercise 2.3 — Delimited Text Data Logging (`.txt` / `.csv`)
- **Platform:** Python (`pyserial` + File I/O)
- **Description:** Extends the reader script to format and append incoming telemetry streams to an external `.txt` log file.
- **Key Features:** Uses semicolon (`;`) delimiters and trailing CRLF (`\r\n`) formatting to ensure immediate compatibility with Microsoft Excel parsing engines. Features file buffer flushing (`file.flush()`) to prevent data loss on unexpected disconnects.

### 4. Exercise 2.4 — 5-Second Statistical Windowing & Real-Time Matplotlib Plotting
- **Platform:** Python (`pyserial`, `numpy`, `matplotlib`)
- **Description:** Implements an interactive data processing application that buffers telemetry into sliding 5-second windows, computes axis-wise Mean ($\mu$) and Standard Deviation ($\sigma$) using NumPy, and updates a real-time line chart using Matplotlib.
- **Key Features:** Leverages thread-safe asynchronous reading routines or explicit event-loop pauses (`plt.pause`) / `FuncAnimation` to maintain responsive graphics updates without blocking serial frame parsing.

---

## 📂 Project Structure

```text
.
├── LB_IOT_P2_1_Serial_Verification/
│   └── LB_IOT_P2_1_Serial_Verification.ino   # Exercise 1: Arduino IMU UART Telemetry Firmware
├── LB_IOT_P2_2_Python_Serial_Reader/
│   └── serial_reader.py                      # Exercise 2: Basic PySerial Console Terminal Reader
├── LB_IOT_P2_3_Data_Logger/
│   ├── data_logger.py                        # Exercise 3: Semicolon-Delimited File Logging Script
│   └── sensor_data.txt                       # Sample Generated Log File (Excel Compatible)
├── LB_IOT_P2_4_Realtime_Plotter/
│   └── live_plot_stats.py                    # Exercise 4: Real-Time Plotting & 5s Stats Calculation
└── README.md                                 # Repository Documentation
