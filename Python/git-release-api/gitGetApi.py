import urllib.request

def getApi(repo):
    if repo[len(repo)-1:] != "/":
        repo += "/"
    repo = repo.replace(" ", "-")
    print("Successfully Retrieved URL")

    fp = urllib.request.urlopen("https://api.github.com/repos/"+repo+"releases")
    mybytes = fp.read()
    html = mybytes.decode("utf8")
    fp.close()
    print("Successfully Connected API")

    file = open('git-api.json', 'w')
    file.write(html)
    file.close()
    print("Successfully Written JSON")

if __name__ == '__main__':
    repo = input("<user>/<repo>/ : ")
    getApi(repo)
