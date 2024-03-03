//# include <DTH.h>
#include "DHT.h"
# include <LiquidCrystal.h>
# define DHT_PIN 3
# define DHT_TYPE DHT11
DHT dht(DHT_PIN,DHT_TYPE);

LiquidCrystal lcd(13,12,11,10,9,8);
//LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

byte customChar[] = {
  B00000,
  B01010,
  B11111,
  B11111,
  B01110,
  B00100,
  B00000,
  B00000
};

int voltage=A0;
int readval;
float Rref=100000;
float res;
float volt;
/////////////
int pin_x=A2;
int pin_y=A1;
int val_x,val_y;
int sw_pin=2;
/////////////

int rain_analog =A3;
int rain_digital=3;
int rain_value;
///////////////

String precipitation;

void setup() {
  Serial.begin(9600);
  lcd.begin(16,2);
  dht.begin();
  pinMode(sw_pin,INPUT);
  digitalWrite(sw_pin,HIGH);
  lcd.print("T:");
  lcd.setCursor(7,0);
  lcd.print("H:");

  lcd.createChar(0, customChar);
  lcd.setCursor(0, 0); // Set cursor position to first row
  //lcd.print(customChar);
  //lcd.write(byte(0));
}

void loop() {
  readval=analogRead(voltage);
  volt=readval*5.0/1023;
  //Serial.println(volt);
  res= ((( 5* Rref)/volt)-Rref);
  //potentiometer for 100 000
  Serial.print("resistance: ");
  res=res*136/100000;
  Serial.print(res);

  val_x=analogRead(pin_x);
  Serial.print(" xvalue ");
  Serial.print(val_x);
  val_y=analogRead(pin_y);
  Serial.print(" yvalue ");
  Serial.print(val_y);

  int value=analogRead(A3);
  Serial.print(" rainvalue ");
  Serial.print(value);


  float temperature=dht.readTemperature();
  float humidity=dht.readHumidity();

  lcd.setCursor(2,0);
  lcd.print(temperature,1);
  Serial.print(" temp: ");
  Serial.print(temperature);
  lcd.setCursor(9,0);
  lcd.print(humidity,1);
  Serial.print(" humidity: ");
  Serial.println(humidity);

  precipitation=Serial.readString();
  lcd.setCursor(0,1);
  lcd.print("pred_rain:");
  lcd.print(precipitation);


  delay(1000);

}
