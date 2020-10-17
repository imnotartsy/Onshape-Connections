/*
This example creates a client object that connects and transfers
data using always SSL.

It is compatible with the methods normally related to plain
connections, like client.connect(host, port).

Written by Arturo Guadalupi
last revision November 2015

*/

#include <SPI.h>
#include <WiFiNINA.h>
#include <TimeLib.h>

#include "sha256.h"
#include "base64.hpp"

const int BUTTON_PIN = 10;

char ssid[] = "Hawk's Pancakes"; //  your network SSID (name)
char pass[] = "catsarelovecatsarelife";    // your network password (use for WPA, or use as key for WEP)

int status = WL_IDLE_STATUS;
// if you don't want to use DNS (and reduce your sketch size)
// use the numeric IP instead of the name for the server:
char server[] = "cad.onshape.com";

WiFiSSLClient client;

void setup () {
  pinMode(BUTTON_PIN, INPUT);
  
  randomSeed(analogRead(0));
  //Initialize serial and wait for port to open:
  Serial.begin(9600);
  while (!Serial); // wait for serial port to connect. Needed for native USB port only

  // check for the presence of the shield:
  if (WiFi.status() == WL_NO_SHIELD) {
    Serial.println("WiFi shield not present");
    // don't continue:
    while (true);
  }

  Serial.println(WiFi.firmwareVersion());

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
  
//  Serial.print("\nStarting connection to server...");
//  // if you get a connection, report back via serial:
//  makeRequest("GET", "/api/documents/4e7fba700f1180e3f3befacf");
//  makeRequest("GET", "/api/documents/d/4e7fba700f1180e3f3befacf/w/3648faa98085565850471de3/elements");

//  char input[] = "{\"items\":[{\"href\":\"https://cad.onshape.com/api/metadata/d/4e7fba700f1180e3f3befacf/w/3648faa98085565850471de3/e/8c27f3aa9b04e06bf7647cc6/p/JHD?configuration=default\",\"properties\":[{\"propertyId\":\"57f3fb8efa3416c06701d60c\",\"value\":{\"isGenerated\":false,\"color\":{\"red\":255,\"green\":0,\"blue\":0},\"opacity\":255}}]}]}";
//  makeRequest("POST", "/api/metadata/d/4e7fba700f1180e3f3befacf/w/3648faa98085565850471de3/e/8c27f3aa9b04e06bf7647cc6/p/JHD", input);

}

bool stopped = false;
int prevVal = 0;

void loop () {
  int val = digitalRead(BUTTON_PIN);
  if (val != prevVal) {
    Serial.println("Button is now " + String(val ? "" : "not") + " pressed!");
    if (val) {
      char input[] = "{\"items\":[{\"href\":\"https://cad.onshape.com/api/metadata/d/4e7fba700f1180e3f3befacf/w/3648faa98085565850471de3/e/8c27f3aa9b04e06bf7647cc6/p/JHD?configuration=default\",\"properties\":[{\"propertyId\":\"57f3fb8efa3416c06701d60c\",\"value\":{\"isGenerated\":false,\"color\":{\"red\":255,\"green\":0,\"blue\":0},\"opacity\":255}}]}]}";
      makeRequest("POST", "/api/metadata/d/4e7fba700f1180e3f3befacf/w/3648faa98085565850471de3/e/8c27f3aa9b04e06bf7647cc6/p/JHD", input);
    } else {
      char input[] = "{\"items\":[{\"href\":\"https://cad.onshape.com/api/metadata/d/4e7fba700f1180e3f3befacf/w/3648faa98085565850471de3/e/8c27f3aa9b04e06bf7647cc6/p/JHD?configuration=default\",\"properties\":[{\"propertyId\":\"57f3fb8efa3416c06701d60c\",\"value\":{\"isGenerated\":false,\"color\":{\"red\":165,\"green\":165,\"blue\":165},\"opacity\":255}}]}]}";
      makeRequest("POST", "/api/metadata/d/4e7fba700f1180e3f3befacf/w/3648faa98085565850471de3/e/8c27f3aa9b04e06bf7647cc6/p/JHD", input);
    }

  }
  prevVal = val;
}


void printWifiStatus () {
  // print the SSID of the network you're attached to:
  Serial.print("SSID: ");
  Serial.println(WiFi.SSID());

  // print your WiFi shield's IP address:
  IPAddress ip = WiFi.localIP();
  Serial.print("IP Address: ");
  Serial.println(ip);

  // print the received signal strength:
  long rssi = WiFi.RSSI();
  Serial.print("signal strength (RSSI):");
  Serial.print(rssi);
  Serial.println(" dBm");
}

// For authentication signatures
String buildNonce () {
  char c_opts[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
  String nonce = "";
  
  for (int i=0; i < 25; i++)
    nonce += c_opts[ random(sizeof(c_opts)/sizeof(char) - 1) ];
  
  return nonce;
}

String utcString () {
  unsigned long t = WiFi.getTime();
  
  String dayofweek = "DAYOFWEEK";
  String monthstr = "MONTH";
  int date = day(t);
  
  
  int h = hour(t);
  int m = minute(t);
  int s = second(t);
  String timestamp = ( (h<10) ? "0"+String(h) : String(h) ) + ":" + ( (m<10) ? "0"+String(m) : String(m) )  + ":" + ( (s<10) ? "0"+String(s) : String(s) ) ;

  switch (month(t)) {
    case 1:
      monthstr = "Jan";
      break;
    case 2:
      monthstr = "Feb";
      break;
    case 3:
      monthstr = "Mar";
      break;
    case 4:
      monthstr = "Apr";
      break;
    case 5:
      monthstr = "May";
      break;
    case 6:
      monthstr = "Jun";
      break;
    case 7:
      monthstr = "Jul";
      break;
    case 8:
      monthstr = "Aug";
      break;
    case 9:
      monthstr = "Sep";
      break;
    case 10:
      monthstr = "Oct";
      break;
    case 11:
      monthstr = "Nov";
      break;
    case 12:
      monthstr = "Dec";
      break;
  }
  
  switch (weekday(t)) {
    case 1:
      dayofweek = "Sun";
      break;
    case 2:
      dayofweek = "Mon";
      break;
    case 3:
      dayofweek = "Tue";
      break;
    case 4:
      dayofweek = "Wed";
      break;
    case 5:
      dayofweek = "Thu";
      break;
    case 6:
      dayofweek = "Fri";
      break;
    case 7:
      dayofweek = "Sat";
      break;
  }
  
  return dayofweek + ", " + ( (date<10) ? "0"+String(date) : String(date) ) + " " + monthstr + " " + year(t) + " " + timestamp + " GMT";
}

String getHmac64 (String payload, String key) {
  Sha256 builder;

  unsigned char keybuf[ key.length() ];
  for (int i=0; i<key.length(); i++)
    keybuf[i] = key[i];

  builder.initHmac((uint8_t*)keybuf, key.length());
  builder.print(payload);

  // Convert hmac to base64
  uint8_t* result = builder.resultHmac();
  unsigned char b64buf[ encode_base64_length(sizeof(result)) ];

  encode_base64((unsigned char *)result, 32, b64buf);

  return String((char *)b64buf);
}

String buildHeaders (String method, String urlpath, String nonce, String date, String contentType, String accessKey, String secretKey) {
  String urlquery = "";
  
  String payload = ( method + "\n" + nonce + "\n" + date + "\n" + contentType
      + "\n" + urlpath + "\n" + urlquery + "\n"
    );
  payload.toLowerCase();

  String auth = "On " + accessKey + ":HmacSHA256:" + getHmac64(payload, secretKey);
  
  return auth;
}

// TODO: Connection: keep-alive only connect to server on setup (for faster requests)
// https://github.com/espressif/arduino-esp32/issues/653#issuecomment-425645575
// https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwij3Omlq87qAhWodN8KHQLAC8oQFjAAegQIAhAB&url=https%3A%2F%2Fforum.arduino.cc%2Findex.php%3Ftopic%3D376619.0&usg=AOvVaw3kdXk3RHeCWh5Q4SDj4Duc
void makeRequest(String reqType, String path) {
    if (client.connect(server, 443)) {
      Serial.println("Connected to server");
  
      String onNonce = buildNonce();
      String date = utcString();
      String signature = buildHeaders( reqType, path, onNonce, date, "application/json", "ZuQDyqNdTg0sZbuyOyLEY2B4", "gOaFuk0r5IDTCd03tYXlJP8c5KP6lTgZj2bA1l8gzVRtDKz4" );
      
      // Make a HTTP request:
      client.println(reqType + " " + path + " HTTP/1.1");
      client.println("Host: cad.onshape.com");
      client.println("Connection: close");
      
      client.println("Content-Type: application/json");
      client.println("Date: " + date);
      client.println("On-Nonce: " + onNonce);
      client.println("Authorization: " + signature);
      client.println("Accept: application/vnd.onshape.v1+json");
  
      client.println();

      int i=0;
      while (!client.available() && i<1000) {
        delay(10);
        i++;
      }
      
      // Skip headers (we just want JSON at the moment)
      char endOfHeaders[] = "\r\n\r\n";
      client.find(endOfHeaders);
  
      String response;
      char input;
  
      do {
        input = client.read();
        response += input;
      } while(client.available());
  
      Serial.println(response);

      client.stop();
    }
}

/* POST DATA */
void makeRequest(String reqType, String path, char* data) {
    if (client.connect(server, 443)) {
      Serial.println("Connected to server");
  
      String onNonce = buildNonce();
      String date = utcString();
      String signature = buildHeaders( reqType, path, onNonce, date, "application/json", "ZuQDyqNdTg0sZbuyOyLEY2B4", "gOaFuk0r5IDTCd03tYXlJP8c5KP6lTgZj2bA1l8gzVRtDKz4" );
      
      // Make a HTTP request:
      client.println(reqType + " " + path + " HTTP/1.1");
      client.println("Host: cad.onshape.com");
      client.println("Connection: close");
      
      client.println("Content-Type: application/json");
      client.print("Content-Length: ");
      client.println(strlen(data));
      client.println("Date: " + date);
      client.println("On-Nonce: " + onNonce);
      client.println("Authorization: " + signature);
      client.println("Accept: application/vnd.onshape.v1+json");  
      client.println();
      client.println(data);


      int i=0;
      while (!client.available() && i<1000) {
        delay(10);
        i++;
      }
      
      // Skip headers (we just want JSON at the moment)
      char endOfHeaders[] = "\r\n\r\n";
      client.find(endOfHeaders);
  
      String response;
      char input;
  
      do {
        input = client.read();
        response += input;
      } while(client.available());
  
      Serial.println(response);

      client.stop();
    }
}
