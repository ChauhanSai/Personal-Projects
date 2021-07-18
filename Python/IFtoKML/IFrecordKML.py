from IFConnectOld import *
from datetime import datetime
import pytz
import time
import keyboard

def loc():
    state = send_command("airplane.getstate", [], await_response=True)
    print()
    state = json.loads(state)['Location']

    altitude=state['AltitudeLight']/17.4638
    latitude=state['Latitude']
    longitude=state['Longitude']

    return [altitude,latitude,longitude]

if __name__ == '__main__':
    breakLetter = " "
    dateStart = datetime.now().strftime("%m/%d/%y")
    fileTime = datetime.now().strftime("%y%m%d %H.%M.%Sz")
    fileName = "IF {}.kml".format(fileTime)
    kml = open(fileName, 'w')
    kml.write('<?xml version="1.0" encoding="UTF-8"?>\n<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">\n<Document>\n\t<name>Infinite Flight ')
    kml.write(dateStart)
    kml.write('</name>')

    timeBreak = ''
    timeBreak = float(input('How often do you want to send/receive data(seconds): '))
    if timeBreak <= 0.0:
        timeBreak = 1.0

    print('Chosen interval =',timeBreak,'seconds')

    airport1 = input('Outbound Airport(Enter when ready to push): ')
    print('Press "',breakLetter,'" to end flight')
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

    kml.write('</description>\n\t\t<gx:Track>\n\t\t\t<extrude>1</extrude>\n\t\t\t<tessellate>1</tessellate>\n\t\t\t<altitudeMode>absolute</altitudeMode>')

    ##Loop every second to add data to path
    timeStart = time.time()
    tz = pytz.timezone('UTC')
    
    while True:
        if keyboard.is_pressed(breakLetter): break
        kml.write('\n\t\t\t<when>')
        if keyboard.is_pressed(breakLetter): break
        kml.write(datetime.now().strftime("%Y-%m-%d"))
        if keyboard.is_pressed(breakLetter): break
        kml.write('T')
        if keyboard.is_pressed(breakLetter): break
        kml.write(datetime.now(tz).strftime("%H:%M:%S"))
        if keyboard.is_pressed(breakLetter): break
        kml.write('Z</when>')
        if keyboard.is_pressed(breakLetter): break

        temp = loc()
        if keyboard.is_pressed(breakLetter): break
        kml.write('\n\t\t\t<gx:coord>')
        if keyboard.is_pressed(breakLetter): break
        kml.write(str(temp[2]))
        if keyboard.is_pressed(breakLetter): break
        kml.write(' ')
        if keyboard.is_pressed(breakLetter): break
        kml.write(str(temp[1]))
        if keyboard.is_pressed(breakLetter): break
        kml.write(' ')
        if keyboard.is_pressed(breakLetter): break
        kml.write(str(temp[0]/3.281))
        if keyboard.is_pressed(breakLetter): break
        kml.write('</gx:coord>')
        if keyboard.is_pressed(breakLetter): break
        print('Press "',breakLetter,'" to end flight')
        if keyboard.is_pressed(breakLetter): break
        time.sleep(timeBreak - ((time.time() - timeStart) % timeBreak))
        if keyboard.is_pressed(breakLetter): break
    
    ##Run when finished
    kml.write('\n\t\t</gx:Track>\n\t</Placemark>')
    airport2 = input('\n\nInbound Airport(Enter when parked): ')
    airport2 = airport2.replace(breakLetter, "")
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
    kml.write(airport1)
    kml.write('-')
    kml.write(airport2)
    kml.write('</description>')

    kml.write('\n</Document>\n</kml>')
    kml.close()

    print('\n\n',fileName,' sucessfully recorded')
