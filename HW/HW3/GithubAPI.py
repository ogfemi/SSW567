import requests


def getGithubReposAndCommits(UserID):
    if not isinstance(UserID, str):
        return "UserID must be a string!"

    API_BASE_URL_REPOS = "https://api.github.com/users/"+UserID+"/repos"
    API_BASE_URL_COMMITS = "https://api.github.com/repos/"+UserID+"/"
    result = []
    response = requests.get(API_BASE_URL_REPOS)
    if response.status_code != 200:
        return "Invalid UserID response!"
    for Repo in response.json():
        response = requests.get(API_BASE_URL_COMMITS +
                                Repo["name"]+"/commits").json()
        result.append((Repo["name"], Repo["commits"]))
    return result

# print(getGithubReposAndCommits("ogfemi"))
