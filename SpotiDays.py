from tracemalloc import Traceback

from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone
import requests
import os
from json import loads
import random

# Load the .env file
load_dotenv()
# Retrieve the API keys
SPOTIFY_CLIENT_USERNAME = os.getenv("SPOTIFY_CLIENT_USERNAME")
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
LASTFM_USERNAME = os.getenv("LASTFM_USERNAME")
LASTFM_API_KEY = os.getenv("LASTFM_API_KEY")
print("Searching for Secret", SPOTIFY_CLIENT_SECRET)

# Get Access Token
tokenHeaders = {
    "Content-Type": "application/x-www-form-urlencoded"
}
tokenData = {
    "grant_type": "client_credentials",
    "client_id": SPOTIFY_CLIENT_ID,
    "client_secret": SPOTIFY_CLIENT_SECRET
}
token = requests.post('https://accounts.spotify.com/api/token', headers=tokenHeaders, data=tokenData).json()

# Use Access Token
spotifyHeaders = {
    "Authorization": token['token_type'] + " " + token['access_token']
}

dataExistingTracks = []
dataRecentTracks = {}
dataTrackQueue = []

userPlaylistHistory = loads(requests.get(
    'https://api.spotify.com/v1/users/' + SPOTIFY_CLIENT_USERNAME + '/playlists',
    headers=spotifyHeaders).text)

# Find Playlist
playlistFound = False
for item in userPlaylistHistory['items']:
    if item['description'] == SPOTIFY_CLIENT_SECRET:
        dataTrackId = item['id']
        dataYear = item['name'][item['name'].find("202"):item['name'].find("202") + 4]
        print("Found Year", dataYear)
        playlistFound = True

        print(item['tracks']['total'], "tracks added")

        # Get Existing Tracks
        trackHistoryUrl = item['tracks']['href'] + '?limit=100'
        trackHistory = loads(requests.get(trackHistoryUrl, headers=spotifyHeaders).text)

        while True:
            # print(trackHistory)
            for track in trackHistory['items']:
                dataExistingTracks.append(track['track']['name'].lower())
            if trackHistory['next']:
                trackHistoryUrl = trackHistory['next']
                trackHistory = loads(requests.get(trackHistoryUrl, headers=spotifyHeaders).text)
            else:
                break

        # Calculate Start Date
        dateStart = datetime.strptime(dataYear, "%Y") + timedelta(days=item['tracks']['total'] + 1)
        dateEnd = datetime.strptime(dataYear + "1231", "%Y%m%d") + timedelta(days=1)
        if dateEnd > datetime.now():
            dateEnd = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)
        print("Starting from", dateStart.strftime("%B %-d, %Y"))
        print("Until", dateEnd.strftime("%B %-d, %Y"))

        # print(dataExistingTracks)
        break

if not playlistFound:
    print("\nError\n\tYear not found, please make a playlist")
    print("\n\tSecret: " + SPOTIFY_CLIENT_SECRET)

try:
    retry = False
    dateCurrent = dateStart
    while dateCurrent < dateEnd:
        userListeningHistoryPage = 1
        userListeningHistoryUrl = f'http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user={LASTFM_USERNAME}&api_key={LASTFM_API_KEY}&format=json&limit=200&from={str(int(dateCurrent.astimezone(timezone.utc).timestamp()))}&to={str(int((dateCurrent + timedelta(days = 1)).astimezone(timezone.utc).timestamp()))}&page='
        userListeningHistory = loads(requests.get(userListeningHistoryUrl + str(userListeningHistoryPage)).text)

        if len(userListeningHistory['recenttracks']['track']) == 0 or retry:
            i = 1
            while len(userListeningHistory['recenttracks']['track']) == 0 or retry:
                retry = False
                userListeningHistoryUrl = f'http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user={LASTFM_USERNAME}&api_key={LASTFM_API_KEY}&format=json&limit=200&from={str(int((dateCurrent + timedelta(days = i)).astimezone(timezone.utc).timestamp()))}&to={str(int((dateCurrent + timedelta(days = 1 + i)).astimezone(timezone.utc).timestamp()))}&page='
                userListeningHistory = loads(requests.get(userListeningHistoryUrl + str(userListeningHistoryPage)).text)
                i += 1
            print(dateCurrent + timedelta(days = i - 1))

        while len(userListeningHistory['recenttracks']['track']) > 0:
            # print(userListeningHistoryUrl + str(userListeningHistoryPage))
            for track in userListeningHistory['recenttracks']['track']:
                # print(track['date']['#text'])
                # print(track['name'])
                if not track['name'].lower() in dataExistingTracks:
                    try:
                        dataRecentTracks[dateCurrent.strftime("%B %-d, %Y")][track['name']] = dataRecentTracks[dateCurrent.strftime("%B %-d, %Y")].get(track['name']) + 1
                    except TypeError:
                        dataRecentTracks[dateCurrent.strftime("%B %-d, %Y")][track['name']] = 1
                    except KeyError:
                        dataRecentTracks[dateCurrent.strftime("%B %-d, %Y")] = {}
                        dataRecentTracks[dateCurrent.strftime("%B %-d, %Y")][track['name']] = 1
            userListeningHistoryPage += 1
            userListeningHistory = loads(requests.get(userListeningHistoryUrl + str(userListeningHistoryPage)).text)

        if len(dataRecentTracks) == 0:
            retry = True
            continue

        print("Top tracks on", dateCurrent.strftime("%B %-d, %Y"))
        dataRecentTrackMax = max(list(dataRecentTracks[dateCurrent.strftime("%B %-d, %Y")].values()))
        dataPossibleTracks = []
        i = 1
        for track in dataRecentTracks[dateCurrent.strftime("%B %-d, %Y")]:
            if dataRecentTracks[dateCurrent.strftime("%B %-d, %Y")][track] == dataRecentTrackMax:
                dataPossibleTracks.append(track)
                print(str(i) + ":", track)
                i += 1

        if len(dataPossibleTracks) > 1:
            selection = input("What track should I add? ")
            if "track_queue" in selection: # Debug option
                print(dataTrackQueue)
                selection = input("What track should I add? ")
            elif "existing_tracks" in selection: # Debug option
                print(dataExistingTracks)
                selection = input("What track should I add? ")
            try:
                dataTrackQueue.append(dataPossibleTracks[int(selection) - 1])
            except ValueError:
                dataTrackQueue.append(random.choice(dataPossibleTracks))
                print(dataTrackQueue[len(dataTrackQueue) - 1])
        else:
            dataTrackQueue.append(dataPossibleTracks[0])
        dataExistingTracks.append((dataTrackQueue[len(dataTrackQueue) - 1]).lower())
        print()

        dateCurrent = dateCurrent + timedelta(days=1)
        dataRecentTracks = {}
except:
    print("\nError\n\t", dateCurrent.strftime("%B %-d, %Y"))
    print(userListeningHistory)
    print(dataTrackQueue)
    print()

if len(dataTrackQueue) > 0:
    print("Tracks to add: ")
    for track in dataTrackQueue:
        print(track)

print(dataYear, "complete")