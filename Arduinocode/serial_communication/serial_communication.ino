#include <dht.h>
#define dht_apin A0

dht DHT;

int r = 9;
int g = 10;
int b = 11;

int data[3];

String value;

unsigned long prevMillis = 0;
const long interval = 5000;

void setup(){
  pinMode(r, OUTPUT);
  pinMode(g, OUTPUT);
  pinMode(b, OUTPUT);
  pinMode(potentie, INPUT);
  
  Serial.begin(9600);
  delay(1500); 
}

void loop(){
  unsigned long currentMillis = millis();
  
  if (currentMillis - prevMillis >= interval){
    prevMillis = currentMillis;
    DHT.read11(dht_apin);
    Serial.print(DHT.temperature);
    Serial.print(',');
    Serial.print(DHT.humidity);
    Serial.print('\n');
    
  }
  else{
    while(Serial.available() >= 4){
      value = Serial.read();
      if (bool(value) == true){
        for (int i = 0; i<3; i++){
            data[i] = Serial.read();
        }
      }
    }
  }    

  analogWrite(r, data[0]);
  analogWrite(g, data[1]);
  analogWrite(b, data[2]);
}
