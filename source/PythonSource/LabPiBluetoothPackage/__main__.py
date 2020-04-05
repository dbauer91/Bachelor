from .Service import BluetoothService
from .Service import DatabaseService
from tkinter import *

def buttonCallback(clientIdentifier: int):
    print("alwdkjwa")

def refreshCallback():
    clients = bluetoothService.scan()

def main():
    buttons = []

    bluetoothService = BluetoothService.BluetoothService()
    
    window = Tk()
    window.wm_title("LabPi Bluetooth Verbindung")
    window.config(background="#FFFFFF")
    
    selectionFrame = Frame(window, width=200, height=300)
    selectionFrame.grid(row=0, column=0, padx=2, pady=2)
    statusFrame = Frame(window, width=200, height=23)
    statusFrame.grid(row=1, column=0, padx=2, pady=2)
    
    statusLabel = Label(statusFrame, text="Initialisierung...")
    statusLabel.grid(row=0, column=0, padx=2, pady=2)
    
    try: 
        while True:
            window.update()

        clients = bluetoothService.scan()

        for client in clients:
            button = Button(selectionFrame, text=client[1], command=buttonCallback);
            button.pack()
            buttons.append(button);

       

    except:
        print("Bluetooth Error!") 

if __name__ == "__main__":
    
# execute only if run as a script
    main()
