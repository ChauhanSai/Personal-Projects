import urllib.request
import webbrowser
from json import loads
from datetime import datetime
import pyautogui
from time import sleep
import imdb

headers = {
  'Content-Type': 'application/json',
  'trakt-api-version': '2',
}
request = urllib.request.Request('https://api.trakt.tv/users/saic06/ratings/', headers=headers)
response_body = urllib.request.urlopen(request).read()
ia = imdb.IMDb()

format = str(response_body)[2:-1].replace("\\", "")
data = loads(format)

dateT = datetime.strptime(open("dateT.txt").readlines()[0], "%Y-%m-%dT%H:%M:%S.000Z")
print("Loading ratings since:", dateT)

webbrowser.open("https://trakt.tv/users/saic06/ratings/")
input("Awaiting Web Browser Start...\nStart?")

for i in data:
    if datetime.strptime(i['rated_at'], "%Y-%m-%dT%H:%M:%S.000Z") > dateT:
        rating = i['rating']
        type = i['type']
        id = ""
        if type == 'movie':
            title = i['movie']['title']
            id = i['movie']['ids']['imdb']
        if type in ['season', 'show', 'episode']:
            show = i['show']['title']
            id = i['show']['ids']['imdb']
            season = ""
            episode = ""
            title = " "
            if type == 'season':
                try:
                    id = i['season']['ids']['imdb']
                except KeyError:
                    continue
                season = str(i['season']['number'])
                episode = " "
            if type == 'episode':
                title += i['episode']['title']
                try:
                    id = i['episode']['ids']['imdb']
                except KeyError:
                    continue
                season = str(i['episode']['season'])
                episode = "." + str(i['episode']['number']) + " "
            title = season + episode + show + title

        print(type.title() + ": '" + title + "' rated", rating)
        try:
            if ".0" in str(ia.get_movie(id[2:]).data['rating']):
                add = 0
                mult = 20.1
            else:
                add = 25
                mult = 18.2
            print("https://www.imdb.com/title/" + id + "/ratings")
            webbrowser.open("https://www.imdb.com/title/" + id + "/ratings")
            sleep(7)
            pyautogui.click(626, 483)
            sleep(2)
            pyautogui.click(635 + add + mult * rating, 488)
            pyautogui.click(635 + add + mult * rating, 488)
            sleep(2)
        except TypeError:
            print("Not rateable on IMDB")
        continue
    else:
        open("dateT.txt", "w").write(data[0]['rated_at'])
        break
