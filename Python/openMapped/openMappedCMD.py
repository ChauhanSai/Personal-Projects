import json

import folium
from os import listdir
from os.path import isfile, join

mm = folium.Map(zoom_start=15, tiles="Stamen Terrain", attr="Map tiles by Stamen Design, CC BY 3.0 — Map data © OpenStreetMap contributors")
folium.TileLayer(
    tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
    attr='Esri', name='Esri Satellite', overlay=False, control=True).add_to(mm)


def start(fileName):
    data = open(fileName, "r")
    file = data.readlines()
    data.close()
    m = folium.Map(zoom_start=15, tiles="Stamen Terrain", attr="Map tiles by Stamen Design, CC BY 3.0 — Map data © OpenStreetMap contributors")
    folium.TileLayer(
        tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
        attr='Esri', name='Esri Satellite', overlay=False, control=True).add_to(m)
    return file, m, fileName


def kml(send):
    file, m, fileName = send
    names = []
    points = []
    route = []
    routeZ = []
    nameKey = "<name>"
    pointKey = "<coordinates>"
    routeKey = "<gx:coord>"
    i = 0
    for line in file:
        if nameKey in line:
            if i > 0:
                names.pop()
            line = line.strip()[len(nameKey):-len(nameKey) - 1]
            names.append(line)
            i = 1
        if pointKey in line:
            line = line.strip()[len(pointKey):-len(pointKey) - 1 - 2].split(",")
            points.append([float(line[1]), float(line[0])])
            i = 0
        if routeKey in line:
            line = line.strip()[len(routeKey):-len(routeKey) - 1].split(" ")
            routeZ.append(float(line.pop(2))) # altitude in meters
            line = (float(line[1]), float(line[0]))
            route.append(line)
        if i > 0:
            i += 1
            if i > 4:
                i = 0
                names.pop()
                continue
    if len(names) == 0 and len(points) == 2:
        names.append("Start")
        names.append("End")
    elif len(names) != len(points):
        names = range(1, len(points) + 1)
    if len(points) != 0:
        folium.Marker(location=points[0], popup=names[0], icon=folium.Icon(icon='circle', prefix='fa')).add_to(m)
        folium.Marker(location=points[0], popup=names[0], icon=folium.Icon(icon='circle', prefix='fa')).add_to(mm)
        folium.Marker(location=points[1], popup=names[1], icon=folium.Icon(icon='circle', prefix='fa')).add_to(m)
        folium.Marker(location=points[1], popup=names[1], icon=folium.Icon(icon='circle', prefix='fa')).add_to(mm)
    folium.PolyLine(route, color='white', weight=6, opacity=1).add_to(m)
    folium.PolyLine(route, color='white', weight=6, opacity=1).add_to(mm)

    # CALCULATE COLORS
    ground_level = max(routeZ[0], routeZ[len(routeZ) - 1])
    for i in range(len(routeZ)):
        routeZ[i] -= ground_level # normalize altitude to simulate barometric pressure
    colors = [('#FFE062', 100),
        ('#FFEA00', 200),
        ('#F0FF00', 300),
        ('#CCFF00', 400),
        ('#42FF00', 600),
        ('#1EFF00', 800),
        ('#00FF0C', 1000),
        ('#00FF36', 1200),
        ('#00FF72', 1500),
        ('#00FF9C', 2000),
        ('#00FFD2', 2500),
        ('#00FFE4', 3000),
        ('#00EAFF', 3500),
        ('#00C0FF', 4000),
        ('#00A8FF', 4500),
        ('#0096FF', 5000),
        ('#0078FF', 5500),
        ('#0054FF', 6000),
        ('#0030FF', 6500),
        ('#001EFF', 7000),
        ('#0000FF', 7500),
        ('#1200FF', 8000),
        ('#2400FF', 8500),
        ('#3600FF', 9000),
        ('#4E00FF', 9500),
        ('#6000FF', 10000),
        ('#7800FF', 10500),
        ('#9600FF', 11000),
        ('#AE00FF', 11500),
        ('#D800FF', 12000),
        ('#FF00E4', 12500),
        ('#FF0000', 13000)] # trail colors based on altitude in meters
    for j in range(len(colors)):
        cropped_route = []
        for i in range(len(routeZ)):
            if routeZ[i] > colors[j][1]:
                cropped_route.append(route[i])
        if len(cropped_route) > 0:
            folium.PolyLine(cropped_route, color=colors[j][0], weight=6, opacity=1).add_to(m)
            folium.PolyLine(cropped_route, color=colors[j][0], weight=6, opacity=1).add_to(mm)
    m.fit_bounds(m.get_bounds(), padding=(30, 30))
    m.save(fileName[:-4] + ".html")
    print(fileName[:-4] + ".html")


def gpx(send):
    file, m, fileName = send
    points = []
    route = []
    ele = []
    routeKeyA = "<trkpt "
    routeKeyB = "<wpt "
    eleKey = "<ele>"
    for line in file:
        if routeKeyA in line or routeKeyB in line:
            line = line[line.index("lat=\"")+5:line.index("\">")]
            line = (float(line[:line.index("lon=\"")-2]), float(line[line.index("lon=\"")+5:]))
            route.append(line)
        if eleKey in line:
            line = line.strip()[line.index("<ele>")+4:line.index("</ele>")-6]
            ele.append(float(line))
    points.append(route[0])
    points.append(route[len(route)-1])

    folium.Marker(location=points[0], icon=folium.Icon(icon='circle', prefix='fa')).add_to(m)
    folium.Marker(location=points[0], icon=folium.Icon(icon='circle', prefix='fa')).add_to(mm)
    folium.Marker(location=points[1], icon=folium.Icon(icon='circle', prefix='fa')).add_to(m)
    folium.Marker(location=points[1], icon=folium.Icon(icon='circle', prefix='fa')).add_to(mm)
    folium.PolyLine(route, color='red', weight=6, opacity=1).add_to(m)
    folium.PolyLine(route, color='red', weight=6, opacity=1).add_to(mm)

    # CALCULATE COLORS
    if len(ele) > 1:
        base = max(ele[0], ele[len(ele) - 1])
        for i in range(len(ele)):
            ele[i] -= base
        color = ["#f9ec60", "#72f960", "#60f9a4", "#70f8e0", "#4bd7e4", "#4bb0e4", "#4242db", "#854be4", "#e249d2",
                 "#ffffff"]
        height = [200, 1500, 5000, 8000, 12000, 15000, 20000, 35000, 40000, 43000]
        for j in range(len(color)):
            arr = []
            for i in range(len(ele)):
                if ele[i] > height[j]:
                    arr.append(route[i])
            if len(arr) > 0:
                folium.PolyLine(arr, color=color[j], weight=6, opacity=1).add_to(m)
                folium.PolyLine(arr, color=color[j], weight=6, opacity=1).add_to(mm)
    m.fit_bounds(m.get_bounds(), padding=(30, 30))
    m.save(fileName[:-4] + ".html")
    print(fileName[:-4] + ".html")


def geojson(send):
    file, m, fileName = send
    data = open(fileName, "r")
    geo = json.load(data)
    data.close()

    points = []
    route = []
    ele = []

    geo = geo["features"]
    for i in geo:
        if i["geometry"]["type"] == 'Point':
            route.append((i["geometry"]["coordinates"][1], i["geometry"]["coordinates"][0]))
            ele.append(i["properties"]["altitude"])

    points.append(route[0])
    points.append(route[len(route) - 1])

    folium.Marker(location=points[0], icon=folium.Icon(icon='circle', prefix='fa')).add_to(m)
    folium.Marker(location=points[0], icon=folium.Icon(icon='circle', prefix='fa')).add_to(mm)
    folium.Marker(location=points[1], icon=folium.Icon(icon='circle', prefix='fa')).add_to(m)
    folium.Marker(location=points[1], icon=folium.Icon(icon='circle', prefix='fa')).add_to(mm)
    folium.PolyLine(route, color='red', weight=6, opacity=1).add_to(m)
    folium.PolyLine(route, color='red', weight=6, opacity=1).add_to(mm)

    # CALCULATE COLORS
    if len(ele) > 1:
        base = max(ele[0], ele[len(ele) - 1])
        for i in range(len(ele)):
            ele[i] -= base
        color = ["#f9ec60", "#72f960", "#60f9a4", "#70f8e0", "#4bd7e4", "#4bb0e4", "#4242db", "#854be4", "#e249d2",
                 "#ffffff"]
        height = [200, 1500, 5000, 8000, 12000, 15000, 20000, 35000, 40000, 43000]
        for j in range(len(color)):
            arr = []
            for i in range(len(ele)):
                if ele[i] > height[j]:
                    arr.append(route[i])
            if len(arr) > 0:
                folium.PolyLine(arr, color=color[j], weight=6, opacity=1).add_to(m)
                folium.PolyLine(arr, color=color[j], weight=6, opacity=1).add_to(mm)
    m.fit_bounds(m.get_bounds(), padding=(30, 30))
    m.save(fileName[:-8] + ".html")
    print(fileName[:-8] + ".html")


def run(directory, file):
    """
    :param directory: Directory OR Single File
    :type directory: basestring
    :param file:
    :type file: basestring
    :return:
    """
    if directory == "" and file == "":
        directory = input("Directory (absolute): ")
        if directory == "":
            fileList = [input("File: ")]
    elif directory == "":
        fileList = [file]

    if directory != "":
        fileList = [f for f in listdir(directory) if isfile(join(directory, f))]
        for i in range(len(fileList)):
            fileList[i] = join(directory, fileList[i])

    for fileName in fileList:
        if fileName[-4:] == ".kml":
            kml(start(fileName))
        elif fileName[-4:] == ".gpx":
            gpx(start(fileName))
        elif fileName[-8:] == ".geojson":
            geojson(start(fileName))

    if len(fileList) > 1:
        mm.fit_bounds(mm.get_bounds(), padding=(30, 30))
        mm.save(join(directory, "openMapped.html"))
        print(join(directory, "openMapped.html"))


if __name__ == '__main__':
    run("", "")

