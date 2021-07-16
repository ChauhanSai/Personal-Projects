from IFConnectOld import *
import json

def loc():
    state = send_command("airplane.getstate", [], await_response=True)
    print()
    state_dict = json.loads(state)['Location']

    altitude=state_dict['AltitudeLight']/17.4638
    latitude=state_dict['Latitude']
    longitude=state_dict['Longitude']

    return [altitude,latitude,longitude]

if __name__ == '__main__':
    temp = loc()
    print('Alt:',temp[0],'ft Lat:',temp[1],'Long:',temp[2])
    print()
