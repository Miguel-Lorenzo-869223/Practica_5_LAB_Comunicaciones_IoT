// ------------------------------------------------------------
//  Author: Miguel A.Lorenzo
//  Date: 17/09/2026
//  Subject: IoT Communications Laboratory 
//  Master: MSc in Electronic Engineering
//  University: University of Zaragoza EINA/UNIZAR
// ------------------------------------------------------------

#include <Arduino.h>
#include <Arduino_LSM9DS1.h>

// Dynamic data variables
float ax, ay, az;
float gx, gy, gz;
float mx, my, mz;

unsigned long pv_millis_sample = 0;
const long interval_sample = 200; // Muestreo y envío cada 200 ms

// FUNCTIONS DECLARATION
void read_imu();
void printer();

void setup() {
  Serial.begin(115200);
  while (!Serial && millis() < 4000);

  if (!IMU.begin()) {
    Serial.println("Failed to initialize IMU!");
    while (1);
  }
  Serial.print("ax");Serial.print(",");
  Serial.print("ay");Serial.print(",");
  Serial.print("az");Serial.print(",");
  Serial.print("gx");Serial.print(",");
  Serial.print("gy");Serial.print(",");
  Serial.print("gz");Serial.print(",");
  Serial.print("mx");Serial.print(",");
  Serial.print("my");Serial.print(",");
  Serial.print("mz");Serial.println(",");
}

void loop() {
  unsigned long current_millis = millis();

  // Muestrea e imprime los datos en un solo ciclo sincronizado
  if (current_millis - pv_millis_sample >= interval_sample) {
    pv_millis_sample = current_millis;
    read_imu();
    printer();
  }
}

void read_imu() {
  if (IMU.accelerationAvailable()) {
    IMU.readAcceleration(ax, ay, az);
  }
  if (IMU.gyroscopeAvailable()) {
    IMU.readGyroscope(gx, gy, gz);
  }
  if (IMU.magneticFieldAvailable()) {
    IMU.readMagneticField(mx, my, mz);
  }
}

// Envía la muestra en formato CSV limpio (separado por comas y finalizado con \n)
void printer() {
  Serial.print(ax, 3); Serial.print(",");
  Serial.print(ay, 3); Serial.print(",");
  Serial.print(az, 3); Serial.print(",");
  Serial.print(gx, 3); Serial.print(",");
  Serial.print(gy, 3); Serial.print(",");
  Serial.print(gz, 3); Serial.print(",");
  Serial.print(mx, 3); Serial.print(",");
  Serial.print(my, 3); Serial.print(",");
  Serial.println(mz, 3);
}