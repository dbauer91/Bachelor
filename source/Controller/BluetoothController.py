from source.Entity.Measurement import Measurement
from source.Entity.Dataset import Dataset

import bluetooth

class BluetoothController:
    def main():
        print(bluetooth.read_local_bdaddr())
        