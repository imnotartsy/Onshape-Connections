#include <SPI.h>
#include <WiFiNINA.h>

#include "arduino_secret.h" 
#include "wifi_utils.h"
///////please enter your sensitive data in the Secret tab/arduino_secrets.h
char ssid[] = SECRET_SSID;           
char pass[] = SECRET_PASS;    
int keyIndex = 0;                            // your network key Index number (needed only for WEP)

int status = WL_IDLE_STATUS;
// if you don't want to use DNS (and reduce your sketch size)
// use the numeric IP instead of the name for the server:
// IPAddress server(74,125,232,128);  // numeric IP for Google (no DNS)
// char server[] = "rogers.onshape.com";     // name address for Google (using DNS)

// Initialize the Ethernet client library
// with the IP address and port of the server
// that you want to connect to (port 80 is default for HTTP):
WiFiClient client;

void setup() {
  //Initialize serial and wait for port to open:
  Serial.begin(9600);
  delay(5000);
  printHello();
  
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

  // check for the WiFi module:
  if (WiFi.status() == WL_NO_MODULE) {
    Serial.println("Communication with WiFi module failed!");
    // don't continue
    while (true);
  }

  String fv = WiFi.firmwareVersion();
  if (fv < WIFI_FIRMWARE_LATEST_VERSION) {
    Serial.println("Please upgrade the firmware");
  }

  // attempt to connect to Wifi network:
  while (status != WL_CONNECTED) {
    Serial.print("Attempting to connect to SSID: ");
    Serial.println(ssid);
    // Connect to WPA/WPA2 network. Change this line if using open or WEP network:
    status = WiFi.begin(ssid, pass);

    // wait 10 seconds for connection:
    delay(10000);
  }
  Serial.println("Connected to wifi");
  printWifiStatus();

  Serial.println("\nStarting connection to server...");
  // if you get a connection, report back via serial:
  if (client.connect("rogers.onshape.com", 80)) { // HTTPS 443, and HTTP 80  
    Serial.println("connected to server");
    
    // Make a HTTP request:
     client.println("GET /api/assemblies/d/dd3414d7ce4a85936fabc2dd/w/2e1ab461aae1e88b62babc36/e/4272ac4853e79613479909d0 HTTP/1.1");
     client.println("Host:rogers.onshape.com");
    // client.println("GET /predictions?page%5Blimit%5D=2&sort=arrival_time&filter%5Bdirection_id%5D=1&filter%5Bstop%5D=2373 HTTP/1.1");
    // client.println("Host: api-v3.mbta.com"); // 443
     client.println("Content-Type: application/json");
     client.println("Accept: application/json");

//    client.println("GET /predictions?filter%5Bstop%5D=2379 HTTP/1.1");
//    client.println("Host: api-v3.mbta.com");


    /* numbers api example */
    // client.println("GET /jokes/random HTTP/1.1"); // 80
    // client.println("Host: api.icndb.com");

    /* numbers api example */
    // client.println("GET /1729");  // 80
    // client.println("Host: http://numbersapi.com");
    
    // https://rogers.onshape.com/api/partstudios/d/aa5f5cb08903b53f224287e0/w/e1f73355bdbd9a727fdd999e/e/1dac61a51b000e06dd9a37a6/features?
    // https://api-v3.mbta.com/predictions?page%5Blimit%5D=2&sort=arrival_time&filter%5Bdirection_id%5D=1&filter%5Bstop%5D=2373
    // http://api.icndb.com/jokes/random 
  

    /* Onshape headers */
//     client.println("On-Nonce: WbLKbbbj8iIRNhE3pY6DpOd26");
//     client.println("Accept: application/json");
//     client.println("Authorization: On 0hOovSkonuPVQkxaT9qDMnIF:HmacSHA256:Ld5BB+rxx3XeVpsAlZ3zeJvzEuNrbHpPm7teunHo/jM=");
//     client.println("Content-Type: application/json");
//     client.println("Host: Mon, 13 Jul 2020 17:52:04 GMT");
//     client.println("User-Agent: Onshape Python Sample App");
    /* {‘On-Nonce’: ‘WbLKbbbj8iIRNhE3pY6DpOd26’,
     *  ‘Accept’: ‘application/json’,
     *  ‘Authorization’: ‘On 0hOovSkonuPVQkxaT9qDMnIF:HmacSHA256:Ld5BB+rxx3XeVpsAlZ3zeJvzEuNrbHpPm7teunHo/jM=’,
     *  ‘Content-Type’: ‘application/json’,
     *  ‘Date’: ‘Mon, 13 Jul 2020 17:52:04 GMT’,
     *  ‘User-Agent’: ‘Onshape Python Sample App’}
     */
    client.println("Connection: close");
    client.println();
  }
}

void loop() {
  // if there are incoming bytes available
  // from the server, read them and print them:
  while (client.available()) {
    char c = client.read();
    Serial.write(c);
  }

  // if the server's disconnected, stop the client:
  if (!client.connected()) {
    Serial.println();
    Serial.println("disconnecting from server.");
    client.stop();

    // do nothing forevermore:
    while (true);
  }
}

void printWifiStatus() {  
  // print the SSID of the network you're attached to:
  Serial.print("SSID: ");
  Serial.println(WiFi.SSID());

  // print your board's IP address:
  IPAddress ip = WiFi.localIP();
  Serial.print("IP Address: ");
  Serial.println(ip);

  // print the received signal strength:
  long rssi = WiFi.RSSI();
  Serial.print("signal strength (RSSI):");
  Serial.print(rssi);
  Serial.println(" dBm");
}
