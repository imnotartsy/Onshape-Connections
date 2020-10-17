void setup() {
   Serial.begin(9600);
   delay(5000);
   Serial.print("Hello!");

}

void loop() {
//  Serial.println(Serial.available());
//  if(Serial.available() > 0){
//    Serial.println(Serial.read(), DEC);
//  }
//
////  Serial.println("Hello!");
//   delay(500);
//   
  Serial.write("AAAAAAAAAAAAAAAAAAAAAA\n");
  Serial.println("EEEEEEEEEEEEEEEEEEEEEEE\n");
  
  delay(500);
}
