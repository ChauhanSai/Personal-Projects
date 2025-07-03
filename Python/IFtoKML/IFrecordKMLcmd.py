import time
from datetime import datetime

import keyboard
import pytz
import ifcclient

DEBUG = True

def loc(ifc):
    altitude = ifc.get_state_by_name('aircraft/0/altitude_msl')
    latitude = ifc.get_state_by_name('aircraft/0/latitude')
    longitude = ifc.get_state_by_name('aircraft/0/longitude')

    if DEBUG:
        print('Altitude:', altitude, ', Latitude:', latitude, ', Longitude:', longitude)

    return [altitude, latitude, longitude]

if __name__ == '__main__':
    print("Listening for Infinite Flight broadcasts")
    devices = ifcclient.IFCClient.discover_devices(duration=0)
    ifc = ifcclient.IFCClient.connect(devices[0], version=2)  # Version is 2 by default
    print("Connected to Infinite Flight")

    if DEBUG:
        manifest = ifc.dump_manifest()

    breakLetter = " "
    dateStart = datetime.now().strftime("%m/%d/%y")
    fileTime = datetime.now().strftime("%y%m%d %H.%M.%Sz")
    fileName = "IF {}.kml".format(fileTime)
    kml = open(fileName, 'w')
    kml.write(
        '<?xml version="1.0" encoding="UTF-8"?>\n<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">\n<Document>\n\t<name>Infinite Flight ')
    kml.write(dateStart)
    kml.write('</name>')

    try:
        timeBreak = float(input('How often do you want to send/receive data(seconds): '))
    except ValueError:
        print('Invalid input, defaulting to 1 second')
        timeBreak = 1.0
    if timeBreak <= 0.0:
        timeBreak = 1.0

    print('Chosen interval =', timeBreak, 'seconds')

    airport1 = input('Outbound Airport(Enter when ready to push): ')
    print('Press "', breakLetter, '" to end flight')
    kml.write('\n\t<Placemark id="b639b753">\n\t\t<name>')
    kml.write(airport1)
    kml.write('</name>\n\t\t<Point>\n\t\t\t<altitudeMode>clampToGround</altitudeMode>\n\t\t\t<coordinates>')
    airport1Loc = loc(ifc)
    kml.write(str(airport1Loc[2]))  # Longitude
    kml.write(',')
    kml.write(str(airport1Loc[1]))  # Latitude
    kml.write(',0')
    kml.write('</coordinates>\n\t\t</Point>\n\t</Placemark>')

    kml.write('\n\t<Placemark id="02bdda12">\n\t\t<name>flight</name>\n\t\t<description>')

    airplane = ifc.get_state_by_name('aircraft/0/name')
    kml.write('Aircraft: ')
    kml.write(airplane)

    kml.write(
        '</description>\n\t\t<gx:Track>\n\t\t\t<extrude>1</extrude>\n\t\t\t<tessellate>1</tessellate>\n\t\t\t<altitudeMode>absolute</altitudeMode>')

    ##Loop every second to add data to path
    timeStart = time.time()
    tz = pytz.timezone('UTC')

    while True:
        try:
            if keyboard.is_pressed(breakLetter):
                break

            kml.write('\n\t\t\t<when>')
            kml.write(datetime.now().strftime("%Y-%m-%d"))
            kml.write('T')
            kml.write(datetime.now(tz).strftime("%H:%M:%S"))
            kml.write('Z</when>')

            temp = loc(ifc)
            kml.write('\n\t\t\t<gx:coord>')
            kml.write(str(temp[2])) # Longitude
            kml.write(' ')
            kml.write(str(temp[1])) # Latitude
            kml.write(' ')
            kml.write(str(temp[0] / 3.281)) # Altitude, convert feet to meter
            kml.write('</gx:coord>')

            print(f"Press '{breakLetter}' to end flight")
            time.sleep(timeBreak - ((time.time() - timeStart) % timeBreak))
        except KeyboardInterrupt:
            print('\nFlight recording interrupted by user.')
            break

    # Run when finished
    kml.write('\n\t\t</gx:Track>\n\t</Placemark>')
    airport2 = input('\n\nInbound Airport(Enter when parked): ')
    airport2 = airport2.replace(breakLetter, "")
    kml.write('\n\t<Placemark id="58adb2d1">\n\t\t<name>')
    kml.write(airport2)
    kml.write('</name>\n\t\t<Point>\n\t\t\t<altitudeMode>clampToGround</altitudeMode>\n\t\t\t<coordinates>')
    airport2Loc = loc(ifc)
    kml.write(str(airport2Loc[2]))  # Longitude
    kml.write(',')
    kml.write(str(airport2Loc[1]))  # Latitude
    kml.write(',0')
    kml.write('</coordinates>\n\t\t</Point>\n\t</Placemark>')

    kml.write('\n\t<description>')
    kml.write(airport1)
    kml.write('-')
    kml.write(airport2)
    kml.write('</description>')

    kml.write('\n</Document>\n</kml>')
    kml.close()

    print('\n\n', fileName, ' successfully recorded')
