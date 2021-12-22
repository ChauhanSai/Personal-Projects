print("Please open Infinite Flight to start program")

import tkinter as tk
from IFConnectOld import *
from datetime import datetime
import pytz
import time
import keyboard
import os

# Set-up the window
window = tk.Tk()
window.title("IF to KML")
try:
    window.iconbitmap('IFtoKML.ico')
except Exception:
    pass
code = 0
mainFrame = tk.Frame(master=window, width=100, height=150)
mainFrame.pack(padx=5, pady=5)

fileNameFrame = tk.Frame(master=mainFrame, width=150, height=150)
fileNameFrame.pack()
fileNameEntry = tk.Entry(master=fileNameFrame, width=20)
fileNameEntry.pack(side=tk.RIGHT)
fileNameLabel = tk.Label(master=fileNameFrame, text="KML Name", width=15, anchor="e")
fileNameLabel.pack(side=tk.RIGHT)

intervalFrame = tk.Frame(master=mainFrame, width=150, height=150)
intervalFrame.pack()
intervalEntry = tk.Entry(master=intervalFrame, width=20)
intervalEntry.pack(side=tk.RIGHT)
intervalEntry.insert(0, "1")
intervalLabel = tk.Label(master=intervalFrame, text="Interval (sec)", width=15, anchor="e")
intervalLabel.pack(side=tk.RIGHT)

depAirportFrame = tk.Frame(master=mainFrame, width=150, height=150)
depAirportFrame.pack()
depAirportEntry = tk.Entry(master=depAirportFrame, width=20)
depAirportEntry.pack(side=tk.RIGHT)
depAirportLabel = tk.Label(master=depAirportFrame, text="Departure ICAO", width=15, anchor="e")
depAirportLabel.pack(side=tk.RIGHT)

arrAirportFrame = tk.Frame(master=mainFrame, width=150, height=150)
arrAirportFrame.pack()
arrAirportEntry = tk.Entry(master=arrAirportFrame, width=20)
arrAirportEntry.pack(side=tk.RIGHT)
arrAirportLabel = tk.Label(master=arrAirportFrame, text="Arrival ICAO", width=15, anchor="e")
arrAirportLabel.pack(side=tk.RIGHT)

def loc():
    state = send_command("airplane.getstate", [], await_response=True)
    print()
    state = json.loads(state)['Location']

    altitude=state['AltitudeLight']/17.4638
    latitude=state['Latitude']
    longitude=state['Longitude']

    return [altitude,latitude,longitude]

def record():
    global code
    if code == 454:
        stop()
        window.update()
        code = 0
        return None
    else:
        code = 454
    print('testd')
    startButton['text']='Stop'
    aircraftLabel['text']='Aircraft: '
    window.update()
    dateStart = datetime.now().strftime("%m/%d/%y")
    fileTime = datetime.now().strftime("%y%m%d %H.%M.%Sz")
    global fileName
    if fileNameEntry.get() == "":
        fileNameEntry.insert(0,"IF {}.kml".format(fileTime))
    else:
        if fileNameEntry.get()[-4:] != ".kml":
            fileNameEntry.insert(len(fileNameEntry.get()),".kml")
    fileNameEntry['state'] = 'disabled'
    fileName = fileNameEntry.get()
    global kml
    kml = open(fileName, 'w')
    kml.write('<?xml version="1.0" encoding="UTF-8"?>\n<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">\n<Document>\n\t<name>Infinite Flight ')
    kml.write(dateStart)
    kml.write('</name>')

    if intervalEntry.get() == "" or int(intervalEntry.get()) <= 0.0:
        intervalEntry.delete(0, tk.END)
        intervalEntry.insert(0, "1")
    intervalEntry['state'] = 'disabled'
    interval = int(intervalEntry.get())

    if depAirportEntry.get() == "":
        depAirportEntry.insert(0, "Departure")
    if arrAirportEntry.get() == "":
        arrAirportEntry.insert(0, "Arrival")
    depAirportEntry['state'] = 'disabled'
    airport1 = depAirportEntry.get()
    kml.write('\n\t<Placemark id="b639b753">\n\t\t<name>')
    kml.write(airport1)
    kml.write('</name>\n\t\t<Point>\n\t\t\t<coordinates>')
    airport1Loc = loc()
    kml.write(str(airport1Loc[2])) ##Longitude
    kml.write(',')
    kml.write(str(airport1Loc[1])) ##Latitude
    kml.write(',0')
    kml.write('</coordinates>\n\t\t</Point>\n\t</Placemark>')
    
    kml.write('\n\t<Placemark id="02bdda12">\n\t\t<name>flight</name>\n\t\t<description>')

    airplane = send_command("airplane.getinfo", [], await_response=True)
    airplane = json.loads(airplane)['Name']
    kml.write('Aircraft: ')
    kml.write(airplane)
    aircraftLabel['text']+=airplane

    kml.write('</description>\n\t\t<gx:Track>\n\t\t\t<extrude>1</extrude>\n\t\t\t<tessellate>1</tessellate>\n\t\t\t<altitudeMode>absolute</altitudeMode>')

    ##Loop every second to add data to path
    timeStart = time.time()
    tz = pytz.timezone('UTC')

    while code == 454:
        kml.write('\n\t\t\t<when>')
        kml.write(datetime.now().strftime("%Y-%m-%d"))
        kml.write('T')
        kml.write(datetime.now(tz).strftime("%H:%M:%S"))
        kml.write('Z</when>')

        temp = loc()
        coords = str(round(temp[2], 5))
        coords += ', '
        coords += str(round(temp[1], 5))
        coords += ', '
        coords += str(round(temp[0]/3.281))
        posLabel['text']='Coords: '
        posLabel['text']+=coords
        kml.write('\n\t\t\t<gx:coord>')
        kml.write(str(temp[2]))
        kml.write(' ')
        kml.write(str(temp[1]))
        kml.write(' ')
        kml.write(str(temp[0]/3.281))
        kml.write('</gx:coord>')
        window.update()
        time.sleep(interval - ((time.time() - timeStart) % interval))
        window.update()

def stop():
    startButton['text']='Stopping...'
    window.update()
    kml.write('\n\t\t</gx:Track>\n\t</Placemark>')
    arrAirportEntry['state'] = 'disabled'
    airport2 = arrAirportEntry.get()
    kml.write('\n\t<Placemark id="58adb2d1">\n\t\t<name>')
    kml.write(airport2)
    kml.write('</name>\n\t\t<Point>\n\t\t\t<coordinates>')
    airport2Loc = loc()
    kml.write(str(airport2Loc[2])) ##Longitude
    kml.write(',')
    kml.write(str(airport2Loc[1])) ##Latitude
    kml.write(',0')
    kml.write('</coordinates>\n\t\t</Point>\n\t</Placemark>')

    kml.write('\n\t<description>')
    kml.write(depAirportEntry.get())
    kml.write('-')
    kml.write(airport2)
    kml.write('</description>')

    kml.write('\n</Document>\n</kml>')
    kml.close()

    startButton['text']='Start'
    fileNameEntry['state'] = 'normal'
    fileNameEntry.delete(0, tk.END)
    intervalEntry['state'] = 'normal'
    intervalEntry.delete(0, tk.END)
    intervalEntry.insert(0, "1")
    depAirportEntry['state'] = 'normal'
    depAirportEntry.delete(0, tk.END)
    arrAirportEntry['state'] = 'normal'
    arrAirportEntry.delete(0, tk.END)
    aircraftLabel['text']='Start to record aircraft data'
    posLabel['text']=fileName
    posLabel['text']+=' sucessfully recorded'
    
    

try:
    startButton = tk.Button(master=mainFrame, text="Start", width=40, height=2, command=record)
    startButton.pack(padx=5, pady=5)
except Exception:
    startButton['text']='Start'

buttonFrame = tk.Frame(master=mainFrame)
buttonFrame.pack()
creditLabel = tk.Label(master=buttonFrame, text="Created By ChauhanSai on GitHub", width=40)
creditLabel.pack()
aircraftLabel = tk.Label(master=buttonFrame, text="Start to record aircraft data", width=40, anchor="w")
aircraftLabel.pack()
posLabel = tk.Label(master=buttonFrame, text=" ", width=40, anchor="w")
posLabel.pack()

# Run the application
window.mainloop()
