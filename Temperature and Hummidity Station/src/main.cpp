#include <Arduino.h>
#include <DHT.h>
#include <WiFi.h>
#include "secrets.h" // Include the secrets header file for WiFi credentials

// put function declarations here:
const int DHTPIN = 4; // Pin where the DHT sensor is connected
const int DHTTYPE = DHT22; // DHT 22 
const char* Wifi_Name = WIFI_SSID; // WiFi name
const char* Wifi_Password = WIFI_PASSWORD; //Wifi password

// auxiliary variables
unsigned long ultima_leitura = 0; // Last reading time

DHT sensor(DHTPIN, DHTTYPE); // Initialize DHT sensor

void setup() {
  sensor.begin(); // Start the DHT sensor
  Serial.begin(115200); // Start the serial communication
  WiFi.begin(Wifi_Name, Wifi_Password); // Connect to WiFi
}

void loop() {
  if (millis() - ultima_leitura >= 5000) {
    ultima_leitura = millis();

    float temperatura_atual = sensor.readTemperature(); // Read temperature
    float humidade_atual = sensor.readHumidity(); // Read humidity

    if (isnan(temperatura_atual) || isnan(humidade_atual)) {
      Serial.println("Falha na leitura do sensor DHT!");
      return;
    }

    Serial.print("Temperatura: ");
    Serial.print(temperatura_atual);
    Serial.print(" °C, Humidade: ");
    Serial.print(humidade_atual);
    Serial.println(" %");
  }
}

