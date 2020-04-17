/*
    Video: https://www.youtube.com/watch?v=oCMOYS71NIU
    Based on Neil Kolban example for IDF: https://github.com/nkolban/esp32-snippets/blob/master/cpp_utils/tests/BLE%20Tests/SampleNotify.cpp
    Ported to Arduino ESP32 by Evandro Copercini
    updated by chegewara

   Create a BLE server that, once we receive a connection, will send periodic notifications.
   The service advertises itself as: 4fafc201-1fb5-459e-8fcc-c5c9c331914b
   And has a characteristic of: beb5483e-36e1-4688-b7f5-ea07361b26a8

   The design of creating the BLE server is:
   1. Create a BLE Server
   2. Create a BLE Service
   3. Create a BLE Characteristic on the Service
   4. Create a BLE Descriptor on the characteristic
   5. Start the service.
   6. Start advertising.

   A connect hander associated with the server starts a background task that performs notification
   every couple of seconds.
*/
#include <BLEDevice.h>
#include <BLEServer.h>
#include <BLEUtils.h>
#include <BLE2902.h>
#include <DHT.h>

BLEServer* pServer = NULL;
BLECharacteristic* pCharacteristicTemp = NULL;
bool deviceConnected = false;
bool oldDeviceConnected = false;


// See the following for generating UUIDs:
// https://www.uuidgenerator.net/
#define SERVICE_UUID        "6424f4f4-a448-4316-a9bf-02c2fc8ab84e"
#define CHARACTERISTIC_UUID "8f918bd0-df4d-4cbb-92d4-195f0ee597cd"


//DHT11 Stuff
#define DHTPIN 18    //Digital pin connected to the DHT Sensor
#define DHTTYPE DHT11
// Initialize DHT sensor.
DHT dht(DHTPIN, DHTTYPE);


class MyServerCallbacks: public BLEServerCallbacks {
    void onConnect(BLEServer* pServer) {
      deviceConnected = true;
    };

    void onDisconnect(BLEServer* pServer) {
      deviceConnected = false;
    }
};

void getTempAndNotify() {
  float temperature = dht.readTemperature();
  Serial.println(temperature);
  //https://github.com/espressif/arduino-esp32/issues/992
  uint8_t tempData[2];
  uint16_t tempValue;
  // multiply by 100 to get 2 digits mantissa and convert into uint16_t
  tempValue = (uint16_t)(temperature *100);
  Serial.println(tempValue);
  // set  LSB of characteristic
  tempData[0] = tempValue;
  // set MSB of characteristic
  tempData[1] = tempValue>>8;
  Serial.println(tempData[0]);
  Serial.println(tempData[1]);
  // set characteristic value
  pCharacteristicTemp->setValue(tempData, 2);
  pCharacteristicTemp->notify();
}


char chipSSID[23];
void getChipSSID() {
  uint64_t chipid = ESP.getEfuseMac(); // The chip ID is essentially its MAC address(length: 6 bytes).
  uint16_t chip = (uint16_t)(chipid >> 32);
  snprintf(chipSSID, 23, "ESP32-%04X%08X", chip, (uint32_t)chipid);
  Serial.println(chipSSID);
}


void setup() {
  Serial.begin(115200);

  getChipSSID();
  
  dht.begin();
  
  // Create the BLE Device
  BLEDevice::init(chipSSID);

  // Create the BLE Server
  pServer = BLEDevice::createServer();
  pServer->setCallbacks(new MyServerCallbacks());

  // Create the BLE Service
  BLEService *pService = pServer->createService(SERVICE_UUID);

  // Create a BLE Characteristic
  pCharacteristicTemp = pService->createCharacteristic(
                      CHARACTERISTIC_UUID,
                      BLECharacteristic::PROPERTY_READ   |
                      BLECharacteristic::PROPERTY_WRITE  |
                      BLECharacteristic::PROPERTY_NOTIFY |
                      BLECharacteristic::PROPERTY_INDICATE
                    );

  // https://www.bluetooth.com/specifications/gatt/viewer?attributeXmlFile=org.bluetooth.descriptor.gatt.client_characteristic_configuration.xml
  // Create a BLE Descriptor
  pCharacteristicTemp->addDescriptor(new BLE2902());

  // Start the service
  pService->start();

  // Start advertising
  BLEAdvertising *pAdvertising = BLEDevice::getAdvertising();
  pAdvertising->addServiceUUID(SERVICE_UUID);
  pAdvertising->setScanResponse(false);
  pAdvertising->setMinPreferred(0x0);  // set value to 0x00 to not advertise this parameter
  BLEDevice::startAdvertising();
  Serial.println("Waiting a client connection to notify...");
}

void loop() {
    // notify changed value
    if (deviceConnected) {
        getTempAndNotify();
        delay(1000); // bluetooth stack will go into congestion, if too many packets are sent, in 6 hours test i was able to go as low as 3ms
    }
    // disconnecting
    if (!deviceConnected && oldDeviceConnected) {
        delay(500); // give the bluetooth stack the chance to get things ready
        pServer->startAdvertising(); // restart advertising
        Serial.println("start advertising");
        oldDeviceConnected = deviceConnected;
    }
    // connecting
    if (deviceConnected && !oldDeviceConnected) {
        // do stuff here on connecting
        oldDeviceConnected = deviceConnected;
    }
}
