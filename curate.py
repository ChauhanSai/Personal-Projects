from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone
import requests
import os
from json import loads
import random
import re
import base64

class Track:
    title: str
    artist: str
    spotify_track_id: str

    def __init__(self, title: str, artist: str, spotify_track_id: str = ""):
        self.title = title
        self.artist = artist
        self.spotify_track_id = spotify_track_id

    def __str__(self) -> str:
        return f"({self.title}, {self.artist}, {self.spotify_track_id})"

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, other) -> bool:
        if isinstance(other, Track):
            return self.title.lower() == other.title.lower()
        elif isinstance(other, str):
            return self.title.lower() == other.lower()
        return False

    def __hash__(self) -> int:
        return hash(self.title.lower())

SORT_BY_ARTIST_FREQUENCY = True

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

def refreshToken(refresh_token):
    load_dotenv()
    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

    auth_header = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
    exchange = requests.post("https://accounts.spotify.com/api/token", data={
        "refresh_token": refresh_token,
        "grant_type": "refresh_token"
    }, headers={
        "Authorization": f"Basic {auth_header}",
        "Content-Type": "application/x-www-form-urlencoded"
    })

    if exchange.status_code != 200:
        return {"status": 401, "error": "Authorization failed"}

    token = exchange.json()
    access_token = token["access_token"]
    # Spotify doesn't always return a new refresh_token
    new_refresh_token = token.get("refresh_token", refresh_token)

    env = open("auth.env", "w")
    env.write(f"ACCESS_TOKEN={access_token}\n")
    env.write(f"REFRESH_TOKEN={new_refresh_token}\n")
    env.close()

    spotify_headers = {
        "Authorization": token['token_type'] + " " + token['access_token']
    }
    return spotify_headers

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

def curate(refresh_token: str = None) -> tuple:
    if refresh_token:
        spotify_headers = refreshToken(refresh_token)
    else:
        spotify_headers = accessToken()

    playlist_id, playlist_year, playlist_length, playlist_tracks_url = getPlaylist(spotify_headers)
    data_existing_tracks = getExisingTracks(spotify_headers, playlist_tracks_url)
    # print(data_existing_tracks)

    # Calculate Start Date
    date_start = datetime.strptime(playlist_year, "%Y") + timedelta(days=playlist_length)
    date_end = datetime.strptime(playlist_year + "1231", "%Y%m%d") + timedelta(days=1)
    if date_end > datetime.now():
        date_end = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    print("\nStarting from", date_start.strftime("%B %-d, %Y"))
    print("Until", date_end.strftime("%B %-d, %Y"), "\n")

    data_track_queue = []

    date_current = date_start
    while date_current < date_end:
        track_selected = getMostPlayedTrack(spotify_headers, date_current, data_existing_tracks + data_track_queue)
        data_existing_tracks.append(track_selected)
        data_track_queue.append(track_selected)

        date_current = date_current + timedelta(days=1)

    print(playlist_year, "curated")

    return playlist_id, data_track_queue

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
        playlist_title = playlist['name']
        playlist_year = max([y for y in re.findall(r'\b\d{4}\b', playlist['name']) if 2008 <= int(y) <= datetime.now().year])
        print("Found '" + playlist_title + "'")

        playlist_length = playlist['tracks']['total']
        print(playlist_length, "tracks added")

        playlist_tracks_url = playlist['tracks']['href']

        return playlist_id, playlist_year, playlist_length, playlist_tracks_url

def getExisingTracks(spotify_headers: dict, playlist_tracks_url: str) -> list[Track]:
    data_existing_tracks = []
    # Get Existing Tracks
    playlist_tracks = loads(requests.get(playlist_tracks_url + '?limit=100', headers=spotify_headers).text)

    while True:
        # print(playlist_tracks)
        for t in playlist_tracks['items']:
            data_existing_tracks.append(Track(t['track']['name'], t['track']['artists'][0]['name'], t['track']['id']))

        if playlist_tracks['next']:
            playlist_tracks = loads(requests.get(playlist_tracks['next'], headers=spotify_headers).text)
        else:
            break

    # print(data_existing_tracks)
    return data_existing_tracks

def getMostPlayedTrack(spotify_headers: dict, date: datetime, existing_tracks: list[Track] = []) -> Track:
    track_frequency = getTrackFrequency(spotify_headers, date, existing_tracks)
    data_possible_tracks = [track for track, freq in track_frequency.items() if freq == max(track_frequency.values())]

    if SORT_BY_ARTIST_FREQUENCY: # If configured
        data_possible_tracks = sortArtistFrequency(data_possible_tracks)

    print("Top tracks for", date.strftime("%B %-d, %Y"))

    i = 1
    for t in data_possible_tracks:
        print(str(i) + ":", t.title + ", " + t.artist)
        i += 1

    if len(data_possible_tracks) == 1:
        track = data_possible_tracks[0]
    else:
        selection = input("What track should I add? ")
        try:
            track = data_possible_tracks[int(selection) - 1]
        except ValueError:
            track = random.choice(data_possible_tracks)
            print(track)

    print()
    return track

def getTrackFrequency(spotify_headers: dict, date: datetime, existing_tracks: list[Track] = [], recur: bool = False) -> dict[Track, int]:
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
                track_id = getSpotifyTrackId(spotify_headers, t['name'], t['artist']['#text'])
                track = Track(t['name'], t['artist']['#text'], track_id)
                # print(track)
                data_track_frequency[track] = data_track_frequency.get(track, 0) + 1
                # print(data_track_frequency[t['name']])

        if int(data_recent_tracks['recenttracks']['@attr']['totalPages']) == 0 or int(data_recent_tracks['recenttracks']['@attr']['totalPages']) == p:
            break
        else:
            p += 1
    # print(data_track_frequency)

    if (not recur) and data_track_frequency == {}:
        d = 1
        while data_track_frequency == {}:
            # print("Trying", (date - timedelta(days=d)).strftime("%B %-d, %Y"))
            data_track_frequency = getTrackFrequency(spotify_headers, date - timedelta(days=d), existing_tracks, True)
            if data_track_frequency == {}:
                # print("Trying", (date + timedelta(days=d)).strftime("%B %-d, %Y"))
                data_track_frequency = getTrackFrequency(spotify_headers, date + timedelta(days=d), existing_tracks, True)
            d += 1

    return data_track_frequency

def sortArtistFrequency(tracks: list[Track]) -> list[Track]:
    # Count how many times each artist appears
    artist_counts = {}
    for track in tracks:
        artist_counts[track.artist] = artist_counts.get(track.artist, 0) + 1

    # Separate tracks into artists appearing multiple times vs. single appearance
    multi_artist_tracks = {}  # artist: list of tracks in order
    single_artist_tracks = []

    for track in tracks:
        if artist_counts[track.artist] > 1:
            if track.artist not in multi_artist_tracks:
                multi_artist_tracks[track.artist] = []
            multi_artist_tracks[track.artist].append(track)
        else:
            single_artist_tracks.append(track)

    # Sort artists by frequency (descending)
    sorted_artists = sorted(multi_artist_tracks.keys(), key=lambda artist: artist_counts[artist], reverse=True)

    # Multi-appearance artists first (sorted by frequency), then single-appearance artists
    tracks_sorted = []
    for artist in sorted_artists:
        tracks_sorted.extend(multi_artist_tracks[artist])
    tracks_sorted.extend(single_artist_tracks)
    # print(tracks_sorted)

    return tracks_sorted

def getSpotifyTrackId(spotify_headers: dict, track_title: str, artist: str = None) -> str:
    tracks = loads(requests.get('https://api.spotify.com/v1/search', headers=spotify_headers, params={
        'q': f'track:{track_title} artist:{artist}',
        'type': 'track'
    }).text)

    try:
        return tracks['tracks']['items'][0]['id']
    except IndexError:
        return ""
    except KeyError:
        return ""

def addTracksToPlaylist(refresh_token: str, playlist_id: str, tracks: list[Track]):
    if not refresh_token:
        return {"status": 400, "error": "Unauthorized - OAuth must be provided"}

    spotify_headers = refreshToken(refresh_token)

    uris = []

    for t in tracks:
        # Pull only track_id and prepend "spotify:track:"
        track_id = t.spotify_track_id
        if track_id:
            uris.append("spotify:track:" + track_id)

    add_items = loads(requests.post(f"https://api.spotify.com/v1/playlists/{playlist_id}/items", headers=spotify_headers, json={
        "uris": uris}).text)

    if add_items['snapshot_id']:
        return {"status": 200}
    else:
        return {add_items['status'], add_items['message']}


if __name__ == '__main__':
    load_dotenv("auth.env", override=True)
    refresh_token = os.getenv("REFRESH_TOKEN")

    if refresh_token is None:
        requests.get("http://127.0.0.1:8080/authorize")
        exit()

    playlist_id, data_track_queue = curate(refresh_token)

    if len(data_track_queue) > 0:
        print("Tracks to add: ")
        for track in data_track_queue:
            print(track)
        print()

        status = addTracksToPlaylist(refresh_token, playlist_id, data_track_queue)
        if status['status'] == 200:
            print("Tracks sucessfully added to playlist")
        else:
            print(status)

    exit()