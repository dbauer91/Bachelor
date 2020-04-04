import bluetooth

class BluetoothService:
    def scan(self) -> []:
        devices = bluetooth.discover_devices(lookup_names=True)
        print(devices)
        return devices

