// Gas + Fire Alarm System
// Arduino Uno

const int gasSensorPin = A0;
const int fireSensorPin = 2;
const int ledPin = 13;
const int buzzerPin = 8;

void setup() {
  pinMode(fireSensorPin, INPUT);
  pinMode(ledPin, OUTPUT);
  pinMode(buzzerPin, OUTPUT);

  Serial.begin(9600);

  digitalWrite(ledPin, LOW);
  digitalWrite(buzzerPin, LOW);
}

void loop() {
  // Read gas sensor
  int gasValue = analogRead(gasSensorPin);

  // Read fire sensor
  int fireValue = digitalRead(fireSensorPin);

  // Display readings
  Serial.print("Gas: ");
  Serial.print(gasValue);
  Serial.print(" | Fire: ");
  Serial.println(fireValue);

  // Check for gas or fire alarm
  if (gasValue >= 300 || fireValue == HIGH) {
    digitalWrite(ledPin, HIGH);
    digitalWrite(buzzerPin, HIGH);

    Serial.println("!!! ALARM !!!");
  }
  else {
    digitalWrite(ledPin, LOW);
    digitalWrite(buzzerPin, LOW);
  }

  delay(500);
}
