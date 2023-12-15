import random
import requests
from datetime import datetime, timedelta
import os
import urllib.request
from json import loads
import unicodedata

code = 0


def createEvent(file, date, startTime, endTime, summary, description, location, repeat):
    """
    Adds a 30-minute event from the startTime to the appendage file
    ex. createEvent(newName, "20220206T232900", "", "")
    :param file: file name
    :type file: basestring
    :param date: %y%m%d
    :type date: basestring
    :param startTime: %-I:%M%p
    :type startTime: basestring
    :param endTime: %-I:%M%p
    :type endTime: basestring
    :param summary: title of event
    :type summary: basestring
    :param description: description of event
    :type description: basestring
    :param location: location of event
    :type location: basestring
    :param repeat: repeating weekly
    :type repeat: boolean
    """
    edit = open(file, 'a')
    edit.write('\nBEGIN:VEVENT')

    edit.write('\nDTSTAMP:')
    edit.write(datetime.now().strftime("%Y%m%dT%H%M%SZ"))

    edit.write('\nUID:')
    for character in summary:
        edit.write(str(ord(character)))

    edit.write('\nDTSTART;TZID=America/Chicago:')
    edit.write(str(datetime.strptime(date, "%y%m%d").strftime("%Y%m%d")) + "T" + str(
        datetime.strptime(startTime, "%I:%M%p").strftime("%H%M%S")))

    edit.write('\nDTEND;TZID=America/Chicago:')
    edit.write(str(datetime.strptime(date, "%y%m%d").strftime("%Y%m%d")) + "T" + str(
        datetime.strptime(endTime, "%I:%M%p").strftime("%H%M%S")))

    if repeat:
        edit.write("\nRRULE:FREQ=WEEKLY;UNTIL=20240524T124000Z")

    edit.write('\nSUMMARY:')
    edit.write(summary)

    edit.write('\nDESCRIPTION:')
    edit.write(description)

    if location != "":
        edit.write("\nLOCATION:" + location)

    edit.write('\nEND:VEVENT')
    edit.close()


def createEventDay(file, date, summary, description, location, repeat):
    """
    Adds a full day event from the startTime to the appendage file
    ex. createEventDay(newName, "20220201", "", "")
    [Alg 2 Hon-RIORDAN] [Bus Info Mgmt I-GRAHAM] [Physics Hon-JENKINS] [AP Comp Sci - S22]
    :param file: file name
    :type file: basestring
    :param date: %y%m%d
    :type date: basestring
    :param summary: title of event
    :type summary: basestring
    :param description: description of event
    :type description: basestring
    :param location: location of event
    :type location: basestring
    :param repeat: repeating weekly
    :type repeat: boolean
    """
    edit = open(file, 'a')
    edit.write('\nBEGIN:VEVENT')

    edit.write('\nDTSTAMP:')
    edit.write(datetime.now().strftime("%Y%m%dT%H%M%SZ"))

    edit.write('\nUID:day-')
    for character in summary:
        edit.write(str(ord(character)))

    edit.write('\nDTSTART;TZID=America/Chicago:')
    edit.write(datetime.strptime(date, "%y%m%d").strftime("%Y%m%d"))

    edit.write('\nDTEND;TZID=America/Chicago:')
    end_date = datetime.strptime(date, "%y%m%d") + timedelta(days=1)
    edit.write(str(end_date.strftime("%Y%m%d")))

    if repeat:
        edit.write("\nRRULE:FREQ=WEEKLY;UNTIL=20240524T124000Z")

    edit.write('\nSUMMARY:')
    edit.write(summary)

    edit.write('\nDESCRIPTION:')
    edit.write(description)

    if location != "":
        edit.write("\nLOCATION:" + location)

    edit.write('\nEND:VEVENT')
    edit.close()


def canvas(url, newName):
    code = 0
    fileName = "C:\\Users\\chauh\\Desktop\\Development\\Scripts\\Python\\iCal Editor\\"
    fileName += url[url.rindex('/') + 1:]
    r = requests.get(url, allow_redirects=True)
    open(fileName, 'wb').write(r.content)

    with open(fileName, 'r', encoding='utf8') as original, open(newName, 'a') as new:
        for line in original:
            if "X-WR-CALNAME:" in line:
                new.write("X-WR-CALNAME:Canvas ICS\n")
                pass
            if "UID:event-assignment" in line:
                code = "T232900"
            if "T000000" in line:
                if code != 0:
                    if "DTSTART;VALUE=DATE:" in line:
                        new.write(line.replace("T000000", code))
                    if "DTEND;VALUE=DATE:" in line:
                        tempA = datetime.strptime(code, "T%H%M%S")
                        end_date = tempA + timedelta(minutes=30)
                        new.write(line.replace("T000000", end_date.strftime("T%H%M%S")))
                        code = 0
                else:
                    if "DTSTART;VALUE=DATE:" in line:
                        new.write(line.replace("T000000", ""))
                    if "DTEND;VALUE=DATE:" in line:
                        tempA = line.replace("T000000", "")
                        tempB = tempA[-9:-1]
                        date_1 = datetime.strptime(tempB, "%Y%m%d")
                        end_date = date_1 + timedelta(days=1)
                        new.write(tempA.replace(tempB, end_date.strftime("%Y%m%d")))
                        code = 0
            else:
                if line == "BEGIN:VCALENDAR\n" or line == "END:VCALENDAR\n" or line == "LOCATION:\n" or line == "SEQUENCE:0\n" or line == "CLASS:PUBLIC\n":
                    pass
                else:
                    try:
                        new.write(line.replace("▪", "-").replace("●", "-").replace("\u2705", "-").replace("️", ""))
                    except UnicodeEncodeError:
                        try:
                            def is_pua(c):
                                return unicodedata.category(c) == 'Co'
                            new.write("".join([char for char in line if not is_pua(char)]))
                        except UnicodeEncodeError:
                            new.write("\n")
        new.close()
        original.close()
        os.remove(fileName)


def loadJson(file):
    request = urllib.request.Request('https://dl.dropboxusercontent.com/s/um0czmrgxsveznn/canvasICS.json?dl=0')
    response_body = urllib.request.urlopen(request).read()

    format = str(response_body)[2:-1].replace("\\r\\n", "").replace("\\xe2\\x80\\x9c", "\"").replace("\\xe2\\x80\\x9d", "\"")
    data = loads(format)

    for i in data:
        try:
            if i['end'] == 'True':
                break
        except KeyError:
            name = i['name']
            date = i['date']
            print(name)
            print(date)
            try:
                if i['weekly'] == 'True':
                    repeat = True
                else:
                    repeat = False
            except KeyError:
                repeat = False
            try:
                description = i['description']
            except KeyError:
                description = ""
            try:
                location = i['location'].replace(",", "\\,")
            except KeyError:
                location = ""
            try:
                start = i['from']
                if len(start) != 7:
                    start = "0" + start
                try:
                    end = i['to']
                    if len(end) != 7:
                        end = "0" + end
                except KeyError:
                    end = datetime.strptime(start, "%I:%M%p") + timedelta(hours=1)
                    end = str(end.strftime("%I:%M%p"))
                createEvent(file, date, start, end, name, description, location, repeat)
                try:
                    if i['addAllDay'] == 'True':
                        createEventDay(file, date, name, description, "", repeat)
                except KeyError:
                    continue
            except KeyError:
                createEventDay(file, date, name, description, location, repeat)


def start(file):
    edit = open(file, 'w')
    edit.write('BEGIN:VCALENDAR\n')
    edit.close()


def end(file):
    edit = open(file, 'a')
    edit.write('\nEND:VCALENDAR')
    edit.close()


def commit(message, file, repoPath):
    import github
    new = open(file, 'r').read()

    g = github.Github('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')  # Personal Access Token
    # or  g = github.Github(login, password)
    repo = g.get_user().get_repo("host")
    contents = repo.get_contents(repoPath, ref="main")
    repo.update_file(contents.path, message, new, contents.sha)

    os.remove(file)


def drop(file, path):
    import pathlib
    import dropbox
    file = [file[:file.rindex("\\") + 1], file[file.rindex("\\") + 1:]]

    filepath = pathlib.Path(file[0]) / file[1]  # Source file object

    d = dropbox.Dropbox(
        app_key="vm2z4s6ibdg9hkd",
        app_secret="epplkrzrptbygx3",
        oauth2_refresh_token="0saR6_ZSybgAAAAAAAAAATOb2EXWCcagvL70Hlz9qtmclj-DbDwP1XqFaLz3a8wB"
    )
    with filepath.open("rb") as f:
        d.files_upload(f.read(), path, mode=dropbox.files.WriteMode("overwrite"))  # Upload with overwrite

    os.remove(file[0] + file[1])


if __name__ == '__main__':
    start('C:\\Users\\chauh\\Desktop\\Development\\Scripts\\Python\\iCal Editor\\canvas.ics') 
    loadJson('C:\\Users\\chauh\\Desktop\\Development\\Scripts\\Python\\iCal Editor\\canvas.ics')
    end('C:\\Users\\chauh\\Desktop\\Development\\Scripts\\Python\\iCal Editor\\canvas.ics')
    drop('C:\\Users\\chauh\\Desktop\\Development\\Scripts\\Python\\iCal Editor\\canvas.ics',
         '/canvas.ics')  
    # commit('Update canvas.ics',
    #        'C:\\Users\\chauh\\Desktop\\Development\\Scripts\\Python\\iCal Editor\\canvas.ics',
    #        '/calendar/canvas.ics')  
