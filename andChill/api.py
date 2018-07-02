import urllib
import requests
import json


def find_movie(title):
    title_encoded = urllib.parse.quote(title)
    index = title[0].lower()
    url = "https://v2.sg.media-imdb.com/suggests/" + index + "/" + title_encoded + ".json"

    r = requests.get(url, headers={'Accept': 'application/json'})

    data = r.content
    title_underscore = title.replace(" ", "_")

    data = data[(6+len(title_underscore)):-1]
    data = json.loads(str(data)[2:-1].replace("\\'", "'"))

    id = data["d"][0]["id"]
    year = data["d"][0]["y"]
    actors = data["d"][0]["s"]

    api_key = "8da59f3dba1924865873677510fb81a3"
    lang = "en-US"
    url_find = "https://api.themoviedb.org/3/find/" + id + "?api_key=" + api_key + "&language=" + lang \
          + "&external_source=imdb_id"

    r = requests.get(url_find, headers={'Accept': 'application/json'})

    data = json.loads(r.content)

    description = data["movie_results"][0]["overview"]
    rating = data["movie_results"][0]["vote_average"]
    picture = "http://image.tmdb.org/t/p/w500" + data["movie_results"][0]["poster_path"]

    url_credits = "https://api.themoviedb.org/3/movie/" + id + "/credits?api_key=" + api_key

    r = requests.get(url_credits, headers={'Accept': 'application/json'})

    data = json.loads(r.content)

    director = None
    if data["crew"][0]["job"] == "Director":
        director = data["crew"][0]["name"]
    else:
        director = "Unknown"

    return {'year': year, 'actors': actors, 'description': description, 'rating': rating, 'picture': picture,
            'director': director}
