import json

file = open('git-api.json',)
data = json.load(file)

count = 0
## Amount of releases
for i in data:
    for j in i:
        if(j == 'assets'):
            count += 1

download_count = 0
## Amount of files- iterate within releases to add downloads up
for i in range(count):
    for j in range((len(data[i]['assets']))):
        download_count += data[i]['assets'][j]['download_count']

## URL of repo
url = data[0]['url'][:data[0]['url'].index('releases')].replace('api', 'www').replace('repos/','')

print('Download Count: ', download_count)
print('from', url)
