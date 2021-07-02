import json

cont="Y"
download_count = 0

while cont == "Y":
    exec(open("git-get-api.py").read())
    
    ## Open JSON
    file = open('git-api.json',)
    data = json.load(file)

    ## Amount of releases
    count = 0
    for i in data:
        for j in i:
            if(j == 'assets'):
                count += 1

    ## Amount of files- iterate within releases to add downloads up
    for i in range(count):
        for j in range((len(data[i]['assets']))):
            download_count += data[i]['assets'][j]['download_count']
    print("Successfully Counted Downloads")

    ## URL of repo
    url = data[0]['url'][:data[0]['url'].index('releases')].replace('api', 'www').replace('repos/','')

    ## Print resluts
    print()
    print('Download Count: ', download_count)
    print('from', url)

    ## Ask to continue
    print()
    cont = input("Continue? Y/N: ")
    if cont=="y":
        cont = "Y"
