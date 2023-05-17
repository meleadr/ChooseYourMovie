# coding: utf-8
import requests
import datetime
from translate import Translator

languages = [
    "en-US",
    "fr-FR",
    "es-ES",
    "de-DE",
    "it-IT",
]

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxYTJkMGQ0YmVjOWQ4NjFhMjFjMmJlMzAwZGI5NDk2NiIsInN1YiI6IjY0NjNjNmI2OGM0NGI5NzgwNzFmMzVhNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.LrT3myEXOkzgpq6nlHWLCEV0aOEsjfW0Bs342-Lu1ZQ",
}


def main():
    print("Languages: ")

    for i in range(len(languages)):
        print(f"{i+1} - {languages[i]}")

    language = int(input("Select a language: "))
    language = languages[language - 1]
    translator = Translator(language)
    name = input(translator.translate("what-name"))
    print(translator.translate("hello"), name)
    lg = language.split("-")[0]
    url = "https://api.themoviedb.org/3/genre/movie/list?language=" + lg

    response = requests.get(url, headers=headers)

    for i in range(len(response.json()["genres"])):
        print(f"{i+1} - {response.json()['genres'][i]['name']}")
    genre = int(input("Select a genre: "))
    genre = response.json()["genres"][genre - 1]["name"]

    recent = input(translator.translate("recent"))
    if recent == "y":
        today = datetime.date.today()

        year = today.year

        url = (
            "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language="
            + language
            + "&page=1&primary_release_year="
            + str(year)
            + "&sort_by=popularity.desc&with_genres="
            + str(genre)
        )
    else:
        url = (
            "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language="
            + language
            + "&page=1&sort_by=popularity.desc&with_genres="
            + str(genre)
        )

    response = requests.get(url, headers=headers)

    for i in range(len(response.json()["results"])):
        print(
            f"{i+1} - {response.json()['results'][i]['title']} - {response.json()['results'][i]['release_date']} - {response.json()['results'][i]['vote_average']}"
        )

    # response = requests.get(url, headers=headers)

    # print(response.text)


if __name__ == "__main__":
    main()
