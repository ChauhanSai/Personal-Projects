# git-release-api
git-release-api is a Python script that retrieves the information of a GitHub repo's releases. Also included is a download counter for a GitHub repository. 

Usage: Using the data given from the API, counting the downloads of a GitHub repository's releases

Definition | Parameters | Usage | File
---------- | ---------- | ----- | ----
getApi(a) | a - repo(string, GitHub repository `<user>/<repo>/`) | Retrieves the GitHub API for a repo and writes it to `git-api.json` | gitGetApi.py
countDownloads(a, b) | a - repo(string, GitHub repository `<user>/<repo>/`), b - downloadCount(int, Starting download count) | Automatically calls getApi(Retrieves the GitHub API for a repo and writes it to 'git-api.json') and counts the downloads for the repository | gitReleaseDownloads.py

### Downloading the script
Download the files attached to the GitHub release found [here](!!!!!!!!!!!!)

### Using the script
