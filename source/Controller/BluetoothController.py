import sys
sys.path.append('../')
from Entity/Measurement import Measurement
from Entity/Dataset import Dataset
import bluetooth
import paho.mqtt as mqtt
import context

class BluetoothController:
    def __init__(self):
        self.mqttClient = mqtt.client.Client()

    def main():
        
        print(bluetooth.read_local_bdaddr())