import json
import urllib
import requests


def find_movie(title):
    title_encoded = urllib.parse.quote(title)
    index = title[0].lower()
    url = "https://v2.sg.media-imdb.com/suggests/" + index + "/" + title_encoded + ".json"

    r = requests.get(url, headers={'Accept': 'application/json'})
    return r
