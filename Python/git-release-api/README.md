# git-release-api
git-release-api is a Python script that retrieves the information of a GitHub repo's releases. Also included is a download counter for a GitHub repository. 

Usage: Using the data given from the API, counting the downloads of a GitHub repository's releases

Definition | Parameters | Usage | Return | File
---------- | ---------- | ----- | ------ | ----
getApi(a) | a - repo(string, GitHub repository `<user>/<repo>/`) | Retrieves the GitHub API for a repo and writes it to `git-api.json` | N/A | gitGetApi.py
countDownloads(a, b) | a - repo(string, GitHub repository `<user>/<repo>/`), b - downloadCount(int, Starting download count) | Automatically calls getApi(Retrieves the GitHub API for a repo and writes it to 'git-api.json') and counts the downloads for the repository | Returns the previous count(b) + current repo count |gitReleaseDownloads.py

## Downloading the script
Download the files attached to the GitHub release found [here](https://github.com/ChauhanSai/Script-Projects/releases/tag/r1)

## Using the script
### Using gitReleaseDownloads.py
Running the script will prompt you to enter a GitHub repo. It will then retrieve the GitHub API and count the downloads for the specific repo. The script will ask you if you'd like to add another count from a different repo and can add them to the total count.
```
<user>/<repo>/ : ChauhanSai/Plasticator-Texture-Pack/
Successfully Retrieved URL
Successfully Connected API
Successfully Written JSON
Successfully Counted Downloads

Download Count:  18
Total Count:  18
from https://www.github.com/ChauhanSai/Plasticator-Texture-Pack/

Continue? Y/N: Y
<user>/<repo>/ : ChauhanSai/Cape-Pack/
Successfully Retrieved URL
Successfully Connected API
Successfully Written JSON
Successfully Counted Downloads

Download Count:  2
Total Count:  20
from https://www.github.com/ChauhanSai/Cape-Pack/

Continue? Y/N: N
```

### Using the API
You can use the provided files and definitions to use the API for your own scripts. Keep in mind that using countDownloads() automatically calls getApi(). See the example file attached to see how you can use the API.
```python
>>>  import gitReleaseDownloads
>>>  
>>>  total = 0
>>>  
>>>  total = gitReleaseDownloads.countDownloads("ChauhanSai/Plasticator-Texture-Pack", total)
>>>  total = gitReleaseDownloads.countDownloads("ChauhanSai/Cape-Pack", total)
```

