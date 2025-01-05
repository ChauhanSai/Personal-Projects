from dotenv import load_dotenv
from datetime import datetime, timedelta, date, time
import requests
import os
from json import loads

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

userPlaylistHistory = loads(requests.get(
    'https://api.spotify.com/v1/users/' + SPOTIFY_CLIENT_USERNAME + '/playlists',
    headers=spotifyHeaders).text)

# Find Playlist
for item in userPlaylistHistory['items']:
    if item['description'] == SPOTIFY_CLIENT_SECRET:
        dataTrackId = item['id']
        dataYear = item['name'][item['name'].find("202"):item['name'].find("202") + 4]
        print("Found Year", dataYear)

        print(item['tracks']['total'], "tracks added")

        # Get Existing Tracks
        trackHistory = loads(requests.get(
            item['tracks']['href'],
            headers=spotifyHeaders).text)
        for track in trackHistory['items']:
            dataExistingTracks.append(track['track']['name'])

        # Calculate Start Date
        dateStart = datetime.strptime(dataYear, "%Y") + timedelta(days=item['tracks']['total'])
        dateEnd = datetime.strptime(dataYear + "1231", "%Y%m%d") + timedelta(days=1)
        print("Starting from", dateStart.strftime("%B %-d, %Y"))

        print(dataExistingTracks)
        break

userListeningHistoryCount = 1
userListeningHistoryUrl = f'http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user={LASTFM_USERNAME}&api_key={LASTFM_API_KEY}&format=json&limit=200&from={str(int(dateStart.timestamp()))}&to={str(int(dateEnd.timestamp()))}&page='
userListeningHistory = loads(requests.get(userListeningHistoryUrl + str(userListeningHistoryCount)).text)

while len(userListeningHistory['recenttracks']['track']) > 0:
    print(userListeningHistoryUrl + str(userListeningHistoryCount))
    for track in userListeningHistory['recenttracks']['track']:
        print(track['date']['#text'])
        print(track['name'])
        if not track['name'] in dataExistingTracks:
            try:
                dataRecentTracks[track['date']['#text'][:11]][track['name']] = dataRecentTracks[track['date']['#text'][:11]].get(track['name']) + 1
            except TypeError:
                dataRecentTracks[track['date']['#text'][:11]][track['name']] = 1
            except KeyError:
                dataRecentTracks[track['date']['#text'][:11]] = {}
                dataRecentTracks[track['date']['#text'][:11]][track['name']] = 1
    userListeningHistoryCount += 1
    userListeningHistory = loads(requests.get(userListeningHistoryUrl + str(userListeningHistoryCount)).text)

print(dataRecentTracks)