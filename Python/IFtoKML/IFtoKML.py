import tkinter as tk
## from IFConnectOld import *
from datetime import datetime
import pytz
import time
import keyboard

# Set-up the window
window = tk.Tk()
window.title("IF to KML")
try:
    window.iconbitmap('IFtoKML.ico')
except Exception:
    pass

mainFrame = tk.Frame(master=window, width=100, height=150)
mainFrame.pack(padx=5, pady=5)

connectionFrame = tk.Frame(master=mainFrame, width=150, height=150)
connectionFrame.pack()
connectionEntry = tk.Label(master=connectionFrame, text="111.111.111", width=18, anchor="w")
connectionEntry.pack(side=tk.RIGHT)
connectionLabel = tk.Label(master=connectionFrame, text="Connected IP", width=15, anchor="e")
connectionLabel.pack(side=tk.RIGHT)

intervalFrame = tk.Frame(master=mainFrame, width=150, height=150)
intervalFrame.pack()
intervalEntry = tk.Entry(master=intervalFrame, width=20)
intervalEntry.pack(side=tk.RIGHT)
intervalEntry.insert(0, "1")
intervalLabel = tk.Label(master=intervalFrame, text="Interval (sec)", width=15, anchor="e")
intervalLabel.pack(side=tk.RIGHT)

intervalFrame = tk.Frame(master=mainFrame, width=150, height=150)
intervalFrame.pack()
intervalEntry = tk.Entry(master=intervalFrame, width=20)
intervalEntry.pack(side=tk.RIGHT)
intervalLabel = tk.Label(master=intervalFrame, text="Departure ICAO", width=15, anchor="e")
intervalLabel.pack(side=tk.RIGHT)

intervalFrame = tk.Frame(master=mainFrame, width=150, height=150)
intervalFrame.pack()
intervalEntry = tk.Entry(master=intervalFrame, width=20)
intervalEntry.pack(side=tk.RIGHT)
intervalLabel = tk.Label(master=intervalFrame, text="Arrival ICAO", width=15, anchor="e")
intervalLabel.pack(side=tk.RIGHT)

def record():
    startButton['text']='Stop'
    startButton['command']=stop
    aircraftLabel['text']='Aircraft: '
    posLabel['text']='Coords: '
    posLabel.pack()

def stop():
    startButton['text']='Start'
    startButton['command']=record
    aircraftLabel['text']='Start to record aircraft data\n'
    posLabel.pack_forget()

try:
    startButton = tk.Button(master=mainFrame, text="Start", width=40, height=2, command=record)
    startButton.pack(padx=5, pady=5)
except Exception:
    startButton['text']='Start'

buttonFrame = tk.Frame(master=mainFrame)
buttonFrame.pack()
creditLabel = tk.Label(master=buttonFrame, text="Created By ChauhanSai on GitHub", width=40)
creditLabel.pack()
aircraftLabel = tk.Label(master=buttonFrame, text="Start to record aircraft data\n", width=40, anchor="w")
aircraftLabel.pack()
posLabel = tk.Label(master=buttonFrame, text="", width=40, anchor="w")

# Run the application
window.mainloop()
