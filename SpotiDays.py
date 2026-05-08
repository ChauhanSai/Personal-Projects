from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone
import requests
import os
from json import loads
import random
from sys import exit
import re

# Load the .env file
load_dotenv()
# Retrieve the API keys
def get_env(key: str) -> str:
    value = os.getenv(key)
    if value is None:
        raise ImportError(f"Missing environment variable {key}")
    return value

keys = {
    "SPOTIFY_CLIENT_USERNAME": get_env("SPOTIFY_CLIENT_USERNAME"),
    "SPOTIFY_CLIENT_ID": get_env("SPOTIFY_CLIENT_ID"),
    "SPOTIFY_CLIENT_SECRET": get_env("SPOTIFY_CLIENT_SECRET"),
    "LASTFM_USERNAME": get_env("LASTFM_USERNAME"),
    "LASTFM_API_KEY": get_env("LASTFM_API_KEY"),
}

def accessToken():
    # Get Access Token
    token_headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    token_data = {
        "grant_type": "client_credentials",
        "client_id": keys["SPOTIFY_CLIENT_ID"],
        "client_secret": keys["SPOTIFY_CLIENT_SECRET"]
    }
    token = requests.post('https://accounts.spotify.com/api/token', headers=token_headers, data=token_data).json()

    # Use Access Token
    spotify_headers = {
        "Authorization": token['token_type'] + " " + token['access_token']
    }
    return spotify_headers

def main():
    spotify_headers = accessToken()

    playlist_id, playlist_year, playlist_length, playlist_tracks_url = getPlaylist(spotify_headers)
    data_existing_tracks = getExisingTracks(playlist_tracks_url, spotify_headers)

    # Calculate Start Date
    dateStart = datetime.strptime(playlist_year, "%Y") + timedelta(days=playlist_length + 1)
    dateEnd = datetime.strptime(playlist_year + "1231", "%Y%m%d") + timedelta(days=1)
    if dateEnd > datetime.now():
        dateEnd = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    print("Starting from", dateStart.strftime("%B %-d, %Y"))
    print("Until", dateEnd.strftime("%B %-d, %Y"))

    dataRecentTracks = {}
    dataTrackQueue = []

    status = 0
    try:
        retry = False
        dateCurrent = dateStart
        while dateCurrent < dateEnd:
            userListeningHistoryPage = 1
            userListeningHistoryUrl = f'http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user={keys["LASTFM_USERNAME"]}&api_key={keys["LASTFM_API_KEY"]}&format=json&limit=200&from={str(int(dateCurrent.astimezone(timezone.utc).timestamp()))}&to={str(int((dateCurrent + timedelta(days=1)).astimezone(timezone.utc).timestamp()))}&page='
            userListeningHistory = loads(requests.get(userListeningHistoryUrl + str(userListeningHistoryPage)).text)

            if len(userListeningHistory['recenttracks']['track']) == 0 or retry:
                i = 1
                while len(userListeningHistory['recenttracks']['track']) == 0 or retry:
                    retry = False
                    userListeningHistoryUrl = f'http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user={keys["LASTFM_USERNAME"]}&api_key={keys["LASTFM_API_KEY"]}&format=json&limit=200&from={str(int((dateCurrent + timedelta(days=i)).astimezone(timezone.utc).timestamp()))}&to={str(int((dateCurrent + timedelta(days=1 + i)).astimezone(timezone.utc).timestamp()))}&page='
                    userListeningHistory = loads(
                        requests.get(userListeningHistoryUrl + str(userListeningHistoryPage)).text)
                    i += 1
                print(dateCurrent + timedelta(days=i - 1))

            while len(userListeningHistory['recenttracks']['track']) > 0:
                # print(userListeningHistoryUrl + str(userListeningHistoryPage))
                for track in userListeningHistory['recenttracks']['track']:
                    # print(track['date']['#text'])
                    # print(track['name'])
                    if not track['name'].lower() in data_existing_tracks:
                        try:
                            dataRecentTracks[dateCurrent.strftime("%B %-d, %Y")][track['name']] = dataRecentTracks[
                                                                                                      dateCurrent.strftime(
                                                                                                          "%B %-d, %Y")].get(
                                track['name']) + 1
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
                if "track_queue" in selection:  # Debug option
                    print(dataTrackQueue)
                    selection = input("What track should I add? ")
                elif "existing_tracks" in selection:  # Debug option
                    print(data_existing_tracks)
                    selection = input("What track should I add? ")
                try:
                    dataTrackQueue.append(dataPossibleTracks[int(selection) - 1])
                except ValueError:
                    dataTrackQueue.append(random.choice(dataPossibleTracks))
                    print(dataTrackQueue[len(dataTrackQueue) - 1])
            else:
                dataTrackQueue.append(dataPossibleTracks[0])
            data_existing_tracks.append((dataTrackQueue[len(dataTrackQueue) - 1]).lower())
            print()

            dateCurrent = dateCurrent + timedelta(days=1)
            dataRecentTracks = {}
    except:
        print("\nError\n\t", dateCurrent.strftime("%B %-d, %Y"))
        print(userListeningHistory)
        print(dataTrackQueue)
        print()
        status = 50

    if len(dataTrackQueue) > 0:
        print("Tracks to add: ")
        for track in dataTrackQueue:
            print(track)

    print(playlist_year, "complete")
    exit(status)

def getPlaylist(spotify_headers: dict) -> tuple:
    user_playlists = loads(requests.get(
        'https://api.spotify.com/v1/users/' + keys["SPOTIFY_CLIENT_USERNAME"] + '/playlists',
        headers=spotify_headers).text)

    print("Searching for Secret", keys["SPOTIFY_CLIENT_SECRET"])
    # Find Playlist
    playlist = None
    for p in user_playlists['items']:
        if p['description'] and p['description'] == keys["SPOTIFY_CLIENT_SECRET"]:
            playlist = p
            break

    if not playlist:
        raise LookupError("Year not found, please make a playlist\nSecret: " + keys["SPOTIFY_CLIENT_SECRET"])
    else:
        playlist_id = playlist['id']
        playlist_year = max([y for y in re.findall(r'\b\d{4}\b', playlist['name']) if 2008 <= int(y) <= datetime.now().year])
        print("Found year:", playlist_year)

        playlist_length = playlist['tracks']['total']
        print(playlist_length, "tracks added")

        playlist_tracks_url = playlist['tracks']['href']

        return playlist_id, playlist_year, playlist_length, playlist_tracks_url

def getExisingTracks(playlist_tracks_url: str, spotify_headers: dict) -> str:
    data_existing_tracks = []
    # Get Existing Tracks
    playlist_tracks = loads(requests.get(playlist_tracks_url + '?limit=100', headers=spotify_headers).text)

    while True:
        # print(playlist_tracks)
        for track in playlist_tracks['items']:
            data_existing_tracks.append(track['track']['name'].lower())

        if playlist_tracks['next']:
            playlist_tracks = loads(requests.get(playlist_tracks['next'], headers=spotify_headers).text)
        else:
            break

    # print(data_existing_tracks)
    return data_existing_tracks

if __name__ == '__main__':
    main()

