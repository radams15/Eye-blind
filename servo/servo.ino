#include <Servo.h>

Servo servoVer; //Vertical Servo
Servo servoHor; //Horizontal Servo
int ledPin = 13;
int ledStat = 0;

int x;
int y;

int defX = 0;
int defY = 0;

int prevX;
int prevY;

void setup()
{
  Serial.begin(9600);
  servoVer.attach(12); //Attach Vertical Servo to Pin 5
  servoHor.attach(4); //Attach Horizontal Servo to Pin 6
  pinMode(ledPin, OUTPUT);

  x = -1;
  y = -1;

  Pos();
}

void ledChange(){
  if(ledStat){
    digitalWrite(ledPin, HIGH);
  }else{
    digitalWrite(ledPin, LOW);
    Serial.println("LOW");
  }
  ledStat ^= 1;
}

void Pos()
{
  if(x == -1){
    x = defX;
  }if(y == -1){
    y = defY;
  }
  if(x == -2){
    x = prevX;
    y = prevY;
    ledChange();
    Serial.println("led");
  }
  
  if(prevX != x || prevY != y)
  {
    /*int servoX = map(x, 600, 0, 70, 179);
    int servoY = map(y, 450, 0, 179, 95);*/
    
    int servoX = map(x, 600, 0, 70, 179);
    int servoY = map(y, 450, 0, 179, 95);

    servoX = min(servoX, 179);
    servoX = max(servoX, 70);
    servoY = min(servoY, 179);
    servoY = max(servoY, 95);     
    
    servoHor.write(servoX);
    servoVer.write(servoY);
  }
}

void loop()
{
  if(Serial.available() > 0)
  {
    if(Serial.read() == 'X')
    {
      x = Serial.parseInt();
      if(Serial.read() == 'Y')
      {
        y = Serial.parseInt();
        //Serial.println(y);
        Pos();
      }
    }
    while(Serial.available() > 0)
    {
      Serial.read();
    }
  }
}
  
