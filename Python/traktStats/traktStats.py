import urllib.request
from json import loads
from datetime import datetime, timedelta, date, time
from imdb import Cinemagoer, IMDbError
import matplotlib.pyplot as plt
from webbrowser import open

def progress(max, i):
    percent = str(round((100 * i) / max)) + "%"
    fill = "█" * round((32 * i) / max) + "∙" * (32 - round((32 * i) / max))
    print(fill, percent)


headers = {
    'Content-Type': 'application/json',
    'trakt-api-version': '2',
}
ia = Cinemagoer()

watchtimeYearbyMonth = {}
watchtimebyDayOfWeek = {"Sun": 0, "Mon": 0, "Tue": 0, "Wed": 0, "Thu": 0, "Fri": 0, "Sat": 0}

watchtime3MonthsbyTimeOfDay = {"Morning": 0, "Mid-day": 0, "Night": 0}
watchtimeMonthbyWeek = {}

ratingsbyNumber = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "10": 0}
ratingsYearbyMonth = {}

dateNowStr = datetime.now().strftime("%Y-%m") + "-01T05%3A00%3A00.000Z"
dateYearStr = (datetime.now() - timedelta(days=365)).strftime("%Y-%m") + "-01T05%3A00%3A00.000Z"
print("From: " + dateYearStr)
print("To: " + dateNowStr)

dateMonthEnd = (datetime.strptime(dateNowStr[0:10], "%Y-%m-%d") - timedelta(days=1)).date()
dateMonth = dateMonthEnd - timedelta(weeks=4)
date3Months = dateMonthEnd - timedelta(weeks=12)

i = dateMonth
while dateMonth <= i <= dateMonthEnd:
    watchtimeMonthbyWeek[i.strftime("%m/%d")] = 0
    i = i + timedelta(days=1)

request = urllib.request.Request(
    'https://api.trakt.tv/users/saic06/history/?start_at=' + dateYearStr + '&end_at=' + dateNowStr + '&limit=1000',
    headers=headers)
response_body = urllib.request.urlopen(request).read()
formatted = str(response_body)[2:-1].replace("\\", "")
history = loads(formatted)
# print(history)

print("\n\nWatched")
count = 0
for i in history:
    date = datetime.strptime(i['watched_at'], "%Y-%m-%dT%H:%M:%S.000Z") - timedelta(hours=5)
    print(date)
    count += 1
    # Data
    type = i['type']
    if type == "movie":  # Watched Movied
        title = i['movie']['title']
        imdbID = i['movie']['ids']['imdb']
        runtime = 110
        try:
            movie = ia.get_movie(imdbID[2:])
            runtime = int(movie.data['runtimes'][0])
        except TypeError:
            pass
        except IMDbError:
            pass
        imdbID = i['movie']['ids']['imdb']
    else:  # Watched Shows
        title = i['show']['title']
        title += " " + i['episode']['title']
        imdbID = i['show']['ids']['imdb']
        runtime = 45
    if imdbID != None:
        imdbID = "(tt" + imdbID[2:] + ")"
    else:
        imdbID = ""
    print(title, runtime, "mins", imdbID)
    # Stats
    if date3Months <= date.date() <= dateMonthEnd:
        i = (date - timedelta(hours=4)).time()
        if time(0, 00) <= i <= time(7, 00):
            watchtime3MonthsbyTimeOfDay["Morning"] += runtime
            print("Morning")
        if time(7, 00) < i <= time(13, 00):
            watchtime3MonthsbyTimeOfDay["Mid-day"] += runtime
            print("Mid-day")
        if time(13, 00) < i <= time(23, 59):
            watchtime3MonthsbyTimeOfDay["Night"] += runtime
            print("Night")
    if dateMonth <= date.date() <= dateMonthEnd:
        watchtimeMonthbyWeek[date.strftime("%m/%d")] += runtime
    date = date.strftime("%b,%a").split(",")
    try:
        watchtimeYearbyMonth[date[0]] += runtime
    except KeyError:
        watchtimeYearbyMonth[date[0]] = 0
        watchtimeYearbyMonth[date[0]] += runtime
    watchtimebyDayOfWeek[date[1]] += runtime
    print(date)
    progress(len(history), count)
    print("\n")

dateNow = datetime.strptime(dateNowStr[:10], "%Y-%m-%d")
dateYear = datetime.strptime(dateYearStr[:10], "%Y-%m-%d")

request = urllib.request.Request('https://api.trakt.tv/users/saic06/ratings/?limit=1000', headers=headers)
response_body = urllib.request.urlopen(request).read()
formatted = str(response_body)[2:-1].replace("\\", "")
ratings = loads(formatted)
# print(ratings)

print("\n\nRated")
count = 0
for i in ratings:
    date = datetime.strptime(i['rated_at'], "%Y-%m-%dT%H:%M:%S.000Z") - timedelta(hours=5)
    if dateNow > date > dateYear:  # Time range
        # Data
        try:
            title = i[i['type']]['title']
            id = i[i['type']]['ids']['imdb']
        except KeyError:
            title = i['show']['title']
            id = i['show']['ids']['imdb']
        rating = i['rating']
        print(title, id, rating, "out of 10")
        # Stats
        date = date.strftime("%b")
        try:
            ratingsYearbyMonth[date][0] += rating
            ratingsYearbyMonth[date][1] += 1
        except KeyError:
            count += 1
            ratingsYearbyMonth[date] = [0, 0]
            ratingsYearbyMonth[date][0] += rating
            ratingsYearbyMonth[date][1] += 1
        ratingsbyNumber[str(rating)] += 1
        print(date)
        progress(12, count)
        print("\n")
    elif date < dateYear:
        break
for i in ratingsYearbyMonth:
    ratingsYearbyMonth[i] = round(int(ratingsYearbyMonth[i][0]) / int(ratingsYearbyMonth[i][1]))

print(watchtimeYearbyMonth)
print(watchtimebyDayOfWeek)
print(watchtime3MonthsbyTimeOfDay)
print(watchtimeMonthbyWeek)
print(ratingsbyNumber)
print(ratingsYearbyMonth)

def traktChart(dict, file, title, xtitle, ytitle, line, bar):
    """
    :type dict: dict
    :type file: string
    :type title: string
    :type xtitle: string
    :type ytitle: string
    :type line: bool
    :type bar: bool
    :return:
    """
    plt.figure(facecolor='#202020')
    ax = plt.axes()
    ax.set_axisbelow(True)
    ax.xaxis.tick_bottom()
    ax.yaxis.tick_left()
    ax.tick_params(axis='x', colors='#2D2D2D')
    ax.tick_params(axis='y', colors='#2D2D2D')
    ax.set_facecolor('#202020')
    ax.spines['bottom'].set_color('#2D2D2D')
    ax.spines['top'].set_color('#2D2D2D')
    ax.spines['right'].set_color('#2D2D2D')
    ax.spines['left'].set_color('#2D2D2D')
    plt.grid(color='#2D2D2D')
    if line:
        x, y = zip(*dict.items())
        plt.plot(x, y, color='#BE1318')
    if bar:
        plt.bar(range(len(dict)), list(dict.values()), align='center', color='#600000')
    plt.xticks(range(len(dict)), list(dict.keys()))
    plt.title(title, color='#ACACAC')
    plt.xlabel(xtitle, color='#ACACAC')
    plt.ylabel(ytitle, color='#ACACAC')
    plt.savefig(file)
    open(file + ".png")


traktChart(watchtimeYearbyMonth, "watchtimeYearbyMonth", "Monthly Watchtime", "Month (1 year)", "Watchtime (mins)", True, True)
traktChart(watchtimebyDayOfWeek, "watchtimebyDayOfWeek", "Watchtime over Days of the Week (1 year sample)", "Day", "Watchtime (mins)", True, True)
traktChart(ratingsbyNumber, "ratingsbyNumber", "Rating Amount by Number", "Rating", "Amount", False, True)
traktChart(watchtime3MonthsbyTimeOfDay, "watchtime3MonthsbyTimeOfDay", "Watchtime by Time of Day", "Time of Day (3 months)", "Watchtime (mins)", False, True)
traktChart(watchtimeMonthbyWeek, "watchtimeMonthbyWeek", "Daily Watchtime", "Day (1 month)", "Watchtime (mins)", False, True)
