#include <ESP32Servo.h>

Servo myServo;
const int servoPin = 16;
String inputString = ""; 

void setup() {
  Serial.begin(115200);
  myServo.attach(servoPin);
  myServo.write(90);
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    int angle = data.toInt();
    if (angle < 0) angle = 0;
    if (angle > 180) angle = 180;
    myServo.write(angle);
  }
}