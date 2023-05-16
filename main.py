# coding: utf-8
import requests
from translate import Translator

languages = [
    "en-US",
    "fr-FR",
    "es-ES",
    "de-DE",
    "it-IT",
]


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
    url = "https://api.themoviedb.org/3/genre/movie/list?language=en"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxYTJkMGQ0YmVjOWQ4NjFhMjFjMmJlMzAwZGI5NDk2NiIsInN1YiI6IjY0NjNjNmI2OGM0NGI5NzgwNzFmMzVhNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.LrT3myEXOkzgpq6nlHWLCEV0aOEsjfW0Bs342-Lu1ZQ",
    }

    response = requests.get(url, headers=headers)

    # url = (
    #     "https://api.themoviedb.org/3/movie/now_playing?language="
    #     + language
    #     + "&page=1"
    # )

    # headers = {
    #     "accept": "application/json",
    #     "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxYTJkMGQ0YmVjOWQ4NjFhMjFjMmJlMzAwZGI5NDk2NiIsInN1YiI6IjY0NjNjNmI2OGM0NGI5NzgwNzFmMzVhNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.LrT3myEXOkzgpq6nlHWLCEV0aOEsjfW0Bs342-Lu1ZQ",
    # }

    # response = requests.get(url, headers=headers)

    print(response.text)


if __name__ == "__main__":
    main()
