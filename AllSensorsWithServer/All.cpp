#include <WiFi.h>
#include <Adafruit_GPS.h>
#include <SoftwareSerial.h>

// WiFi settings
const char* ssid = "your_ssid";
const char* password = "your_password";
const char* serverAddress = "192.168.1.100"; // IP address of your Raspberry Pi
const int serverPort = 3000;
WiFiClient client;

// Sensor pins
const int gasSensorPin = 32; // GPIO 32
const int tempPressureHumiditySensorPin = 33; // GPIO 33
const int measurePin = A0;
const int ledPower = 2;

// Motor control pins
const int rightMotor1 = 26;
const int rightMotor2 = 27;
const int rightMotor3 = 14;
const int leftMotor1 = 12;
const int leftMotor2 = 13;
const int leftMotor3 = 25;

// Ultrasonic sensor pins
const int trigPin = 26; // GPIO 26
const int echoPin = 27; // GPIO 27

// GPS settings
SoftwareSerial mySerial(3, 2); // RX, TX
Adafruit_GPS GPS(&mySerial);
char c;

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

  // Sensor pins setup
  pinMode(gasSensorPin, INPUT);
  pinMode(tempPressureHumiditySensorPin, INPUT);
  pinMode(measurePin, INPUT);
  pinMode(ledPower, OUTPUT);

  // Motor control pins setup
  pinMode(rightMotor1, OUTPUT);
  pinMode(rightMotor2, OUTPUT);
  pinMode(rightMotor3, OUTPUT);
  pinMode(leftMotor1, OUTPUT);
  pinMode(leftMotor2, OUTPUT);
  pinMode(leftMotor3, OUTPUT);

  // Ultrasonic sensor pins setup
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  // GPS setup
  GPS.begin(9600);
  GPS.sendCommand(PMTK_SET_NMEA_OUTPUT_RMCGGA);
  GPS.sendCommand(PMTK_SET_NMEA_UPDATE_1HZ);
  delay(1000);
}

void loop() {
  // Sensor readings
  int gasSensorValue = analogRead(gasSensorPin);
  int tempPressureHumiditySensorValue = analogRead(tempPressureHumiditySensorPin);
  float dustDensity = readDustDensity();
  float carbonMonoxideRatio = readCarbonMonoxideRatio();
  float distance = readUltrasonicDistance();

  // GPS readings
  clearGPS();
  while (!GPS.newNMEAreceived()) {
    c = GPS.read();
  }
  GPS.parse(GPS.lastNMEA());
  float latitude = GPS.latitudeDegrees;
  float longitude = GPS.longitudeDegrees;

  // Movement control
  moveForward();
  delay(2000); // Move forward for 2 seconds
  stopMoving();
  delay(1000); // Wait for 1 second

  // Send sensor data to server
  sendDataToServer(gasSensorValue, tempPressureHumiditySensorValue, dustDensity, carbonMonoxideRatio, distance, latitude, longitude);

  delay(1000); // Delay before next iteration
}

void moveForward() {
  // Right side motors
  digitalWrite(rightMotor1, HIGH);
  digitalWrite(rightMotor2, LOW);
  digitalWrite(rightMotor3, HIGH);

  // Left side motors
  digitalWrite(leftMotor1, LOW);
  digitalWrite(leftMotor2, HIGH);
  digitalWrite(leftMotor3, HIGH);
}

void stopMoving() {
  // Right side motors
  digitalWrite(rightMotor1, LOW);
  digitalWrite(rightMotor2, LOW);
  digitalWrite(rightMotor3, LOW);

  // Left side motors
  digitalWrite(leftMotor1, LOW);
  digitalWrite(leftMotor2, LOW);
  digitalWrite(leftMotor3, LOW);
}

float readDustDensity() {
  // Sensor reading logic
}

float readCarbonMonoxideRatio() {
  // Sensor reading logic
}

float readUltrasonicDistance() {
  // Sensor reading logic
}

void sendDataToServer(int gasSensorValue, int tempPressureHumiditySensorValue, float dustDensity, float carbonMonoxideRatio, float distance, float latitude, float longitude) {
  if (client.connect(serverAddress, serverPort)) {
    String jsonData = "{\"gasSensorValue\":" + String(gasSensorValue) + ",\"tempPressureHumiditySensorValue\":" + String(tempPressureHumiditySensorValue) + ",\"dustDensity\":" + String(dustDensity) + ",\"carbonMonoxideRatio\":" + String(carbonMonoxideRatio) + ",\"distance\":" + String(distance) + ",\"latitude\":" + String(latitude, 6) + ",\"longitude\":" + String(longitude, 6) + "}";
    String httpRequest = "POST /update HTTP/1.1\r\nHost: " + String(serverAddress) + "\r\nContent-Type: application/json\r\nContent-Length: " + String(jsonData.length()) + "\r\n\r\n" + jsonData;
    client.print(httpRequest);
    client.stop();
  } else {
    Serial.println("Connection failed");
  }
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
