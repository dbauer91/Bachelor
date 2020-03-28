from Entity import *
from Service import *
from tkinter import *

def main():
    bluetoothService = BluetoothService()
    databaseService = DatabaseService()
    
    window = Tk()
    window.wm_title("LabPi Bluetooth Verbindung")
    
    selectionFrame = Frame(window, width=200, height=600)
    selectionFrame.grid(row=0, column=0, padx=2, pady=2)
    statusFrame = Frame(window, width=200, height=23)
    statusFrame.grid(row=1, column=0, padx=2, pady=2)
    
    statusLabel = Label(statusFrame, text="Initialisierung...")
    statusLabel.grid(row=0, column=0, padx=2, pady=2)
    
    try: 
        bluetoothService.setup()
    
        clients = bluetoothService.getAvailableClients()
    
        for client in clients:
            clientButton = Button(selectionFrame, text=client.getIdentifier(), command=lambda:
                clientButton.setvar("bg", "#FFFF00")
                if bluetoothService.connect(client.getIdentifier()) == True:
                    clientButton.setvar("bg", "#00FF00")
                    statusLabel.setvar("text", "Verbindung erfolgreich hergestellt")
                else:
                    clientButton.setvar("bg", "#FF0000")
                    statusLabel.setvar("text", "Verbindung konnte nicht hergestellt werden, weitere Informationen sind im Log zu finden")    
            )
    
    except BluetoothError:    

main()