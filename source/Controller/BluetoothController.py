import sys
sys.path.append('../')

from Entity/Measurement import Measurement
from Entity/Dataset import Dataset

import bluetooth
import paho.mqtt as mqtt
import context

class BluetoothController:
    def __init__(self):
        mqttc.on_message = on_message
        mqttc.on_connect = on_connect
        mqttc.on_publish = on_publish
        mqttc.on_subscribe = on_subscribe
        mqttc.username_pw_set(<user>, <pw>)

        self.mqttClient = mqtt.client.Client()
        self.mqttClient.connect(<host>, <port>)

    def main():
        print(bluetooth.read_local_bdaddr())
        
    def on_connect(self.mqttClient, obj, flags, rc):
        print("connect rc: " + str(rc))


    def on_message(self.mqttClient, obj, msg):
        print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))


    def on_publish(self.mqttClient, obj, mid):
        print("mid: " + str(mid))


    def on_subscribe(self.mqttClient, obj, mid, granted_qos):
        print("Subscribed: " + str(mid) + " " + str(granted_qos))

