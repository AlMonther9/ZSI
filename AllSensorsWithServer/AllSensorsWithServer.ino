#include <WiFi.h>
#include <Adafruit_GPS.h>
#include <SoftwareSerial.h>

// WiFi settings
const char* ssid = "A";
const char* password = "@AlMonther0123E";
const char* serverAddress = "192.168.12.166";
const int serverPort = 3000;
WiFiClient client;

// Gas sensor settings
const int gasSensorPin = 32; // GPIO 32

// Temperature, pressure, and humidity sensor settings
const int tempPressureHumiditySensorPin = 33; // GPIO 33

// GPS settings
SoftwareSerial mySerial(3, 2);
Adafruit_GPS GPS(&mySerial);
char c;

// Air quality and dust sensor settings
int measurePin = A0;
int ledPower = 2;
int samplingTime = 280;
int deltaTime = 40;
int sleepTime = 9680;
float voMeasured = 0;
float calcVoltage = 0;
float dustDensity = 0;

// Carbon monoxide sensor settings
const int LED = 2;
const int DO = 8;
float R0 = 0.72;

void setup() {
  Serial.begin(9600);
  delay(10);

  // WiFi setup
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");

  // GPS setup
  GPS.begin(9600);
  GPS.sendCommand(PMTK_SET_NMEA_OUTPUT_RMCGGA);
  GPS.sendCommand(PMTK_SET_NMEA_UPDATE_1HZ);
  delay(1000);

  // Air quality and dust sensor setup
  pinMode(ledPower, OUTPUT);

  // Carbon monoxide sensor setup
  pinMode(LED, OUTPUT);
  pinMode(DO, INPUT);
}

void loop() {
  // Gas sensor reading
  int gasSensorValue = analogRead(gasSensorPin);

  // Temperature, pressure, and humidity sensor reading
  int tempPressureHumiditySensorValue = analogRead(tempPressureHumiditySensorPin);

  // GPS reading
  clearGPS();
  while (!GPS.newNMEAreceived()) {
    c = GPS.read();
  }
  GPS.parse(GPS.lastNMEA());

  // Air quality and dust sensor reading
  digitalWrite(ledPower, LOW);
  delayMicroseconds(samplingTime);
  voMeasured = analogRead(measurePin);
  delayMicroseconds(deltaTime);
  digitalWrite(ledPower, HIGH);
  delayMicroseconds(sleepTime);
  calcVoltage = voMeasured * (5.0 / 1024.0);
  dustDensity = 170 * calcVoltage - 0.1;
  
  // Carbon monoxide sensor reading
  int alarm = 0;
  float sensor_volt = ((float)analogRead(A0) / 1024) * 5.0;
  float RS_gas = (5.0 - sensor_volt) / sensor_volt;
  float ratio = RS_gas / R0;

  // Send data to server
  if (client.connect(serverAddress, serverPort)) {
    String jsonData = "{\"gasSensorValue\":" + String(gasSensorValue) + ",\"tempPressureHumiditySensorValue\":" + String(tempPressureHumiditySensorValue) + ",\"latitudeDegrees\":" + String(GPS.latitudeDegrees, 4) + ",\"longitudeDegrees\":" + String(GPS.longitudeDegrees, 4) + ",\"dustDensity\":" + String(dustDensity) + ",\"carbonMonoxideRatio\":" + String(ratio) + "}";
    String httpRequest = "POST /update HTTP/1.1\r\nHost: " + String(serverAddress) + "\r\nContent-Type: application/json\r\nContent-Length: " + String(jsonData.length()) + "\r\n\r\n" + jsonData;
    client.print(httpRequest);
    client.stop();
  } else {
    Serial.println("Connection failed");
  }

  delay(1000);
}

void clearGPS() {
  while (!GPS.newNMEAreceived()) {
    c = GPS.read();
  }
  GPS.parse(GPS.lastNMEA());

  while (!GPS.newNMEAreceived()) {
    c = GPS.read();
  }
  GPS.parse(GPS.lastNMEA());
}
