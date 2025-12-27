#include <ESP32Servo.h>

Servo myServo;

int servo = 16;
int servoAngle = 90;

void setup() {
 Serial.begin(115200);
 myServo.attach(servo);
}

void loop() {
  if (Serial.available()) {
    servoAngle = Serial.read();
    myServo.write(servoAngle);
    Serial.write(servoAngle);
  }

}
