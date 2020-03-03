import daemon

from BluetoothController import main

with daemon.DaemonContext():
     main()