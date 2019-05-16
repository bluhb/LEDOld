int r = 11;
int g = 10;
int b = 9;

int data[3];




void setup(){
  pinMode(r, OUTPUT);
  pinMode(g, OUTPUT);
  pinMode(b, OUTPUT);
  Serial.begin(9600);
  
}


void loop(){
  while(Serial.available() >= 3){
      for (int i = 0; i<3; i++){
        data[i] = Serial.read();
      }


    int red = map(data[0],0,255,0,180);
    int green = map(data[1],0,255,0,255);
    int blue = map(data[2],0,255,0,180);   
    analogWrite(r, red);
    analogWrite(g, green);
    analogWrite(b, blue);


    

  }
}
