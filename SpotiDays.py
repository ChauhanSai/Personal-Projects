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
    date_start = datetime.strptime(playlist_year, "%Y") + timedelta(days=playlist_length + 1)
    date_end = datetime.strptime(playlist_year + "1231", "%Y%m%d") + timedelta(days=1)
    if date_end > datetime.now():
        date_end = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    print("\nStarting from", date_start.strftime("%B %-d, %Y"))
    print("Until", date_end.strftime("%B %-d, %Y"), "\n")

    data_track_queue = []

    date_current = date_start
    while date_current < date_end:
        track_selected = getMostPlayedTrack(date_current, spotify_headers, data_existing_tracks + data_track_queue)
        data_existing_tracks.append(track_selected.lower())
        data_track_queue.append(track_selected)

        date_current = date_current + timedelta(days=1)

    if len(data_track_queue) > 0:
        print("Tracks to add: ")
        for track in data_track_queue:
            print(track)

    print(playlist_year, "complete")

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

def getExisingTracks(playlist_tracks_url: str, spotify_headers: dict) -> list[str]:
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

def getMostPlayedTrack(date: datetime, spotify_headers: dict, existing_tracks: list[str] = None) -> str:
    data_possible_tracks = getTrackFrequency(date, spotify_headers, existing_tracks)
    print("Top tracks for", date.strftime("%B %-d, %Y"))

    i = 1
    for t in data_possible_tracks:
        print(str(i) + ":", t)
        i += 1

    selection = input("What track should I add? ")
    try:
        track = list(data_possible_tracks.keys())[int(selection) - 1]
    except ValueError:
        track = random.choice(list(data_possible_tracks.keys()))
        print(track)

    print()
    return track

def getTrackFrequency(date: datetime, spotify_headers: dict, existing_tracks: list[str] = None, recur: bool = False) -> dict[str, int]:
    if date >  datetime.now():
        return {}

    data_track_frequency = {}

    p = 1
    while True:
        data_recent_tracks = loads(requests.get('http://ws.audioscrobbler.com/2.0/', params={
            'method': 'user.getrecenttracks',
            'user': keys["LASTFM_USERNAME"],
            'api_key': keys["LASTFM_API_KEY"],
            'format': 'json',
            'limit': 200,
            'from': str(int(date.astimezone(timezone.utc).timestamp())),
            'to': str(int((date + timedelta(days=1)).astimezone(timezone.utc).timestamp())),
            'page': p
        }).text)
        # print(data_recent_tracks)

        for t in data_recent_tracks['recenttracks']['track']:
            # print(t)
            # print(t['name'])
            if not (t['name'].lower() in existing_tracks):
                try:
                    data_track_frequency[t['name']] = data_track_frequency[t['name']] + 1
                except TypeError:
                    data_track_frequency[t['name']] = 1
                except KeyError:
                    data_track_frequency[t['name']] = 1
                # print(data_track_frequency[t['name']])

        if int(data_recent_tracks['recenttracks']['@attr']['totalPages']) == p:
            break
        else:
            p += 1
    # print(data_track_frequency)

    if (not recur) and data_track_frequency == {}:
        d = 1
        while data_track_frequency == {}:
            # print("Trying", (date - timedelta(days=d)).strftime("%B %-d, %Y"))
            data_track_frequency = getTrackFrequency(date - timedelta(days=d), spotify_headers, existing_tracks, True)
            if data_track_frequency == {}:
                # print("Trying", (date + timedelta(days=d)).strftime("%B %-d, %Y"))
                data_track_frequency = getTrackFrequency(date + timedelta(days=d), spotify_headers, existing_tracks, True)
            d += 1

    return data_track_frequency

if __name__ == '__main__':
    main()
