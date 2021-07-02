import json
import gitGetApi

downloadCount = 0

def countDownloads(repo, downloadCount):
    
    gitGetApi.getApi(repo)
    
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
    tempDownloadCount = 0 
    for i in range(count):
        for j in range((len(data[i]['assets']))):
            tempDownloadCount += data[i]['assets'][j]['download_count']
    print("Successfully Counted Downloads")
    downloadCount += tempDownloadCount

    ## URL of repo
    url = data[0]['url'][:data[0]['url'].index('releases')].replace('api', 'www').replace('repos/','')

    ## Print results
    print()
    print('Download Count: ', tempDownloadCount)
    print('Total Count: ', downloadCount)
    print('from', url)
    print()
    return downloadCount

if __name__ == '__main__':
    cont="Y"
    ## Repeat until told to stop
    while cont == "Y":
        repo = input("<user>/<repo>/ : ")
        downloadCount = countDownloads(repo, downloadCount)
        
        ## Ask to continue
        cont = input("Continue? Y/N: ")
        if cont=="y":
            cont = "Y"
