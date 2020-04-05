import bluetooth

class BluetoothService:
    def __init__(self):
        self.devices = []

    def scan(self):
        self.devices = bluetooth.discover_devices(lookup_names=True)
        print(self.devices)
        return self.devices
