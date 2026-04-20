const int GPIO = 2;

void setup() {
  pinMode(GPIO, OUTPUT);
  
  // Elindítjuk a kommunikációt az USB kábelen a laptoppal
  // A 115200 a kommunikáció sebessége
  Serial.begin(115200); 
  Serial.println("ESP32 készen áll! Várakozás a parancsokra...");
}

void loop() {
  // Megnézzük, hogy jött-e valamilyen üzenet a laptoptól
  if (Serial.available() > 0) {
    // Kiolvasunk 1 darab karaktert (betűt vagy számot)
    char parancs = Serial.read(); 
    
    if (parancs == '1') {
      digitalWrite(GPIO, HIGH); // LED bekapcsolása
      Serial.println("LED BEKAPCSOLVA");
    } 
    else if (parancs == '0') {
      digitalWrite(GPIO, LOW);  // LED kikapcsolása
      Serial.println("LED KIKAPCSOLVA");
    }
  }
}