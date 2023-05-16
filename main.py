# coding: utf-8
import requests

languages = [
    "en-US",
    "fr-FR",
    "es-ES",
    "de-DE",
    "it-IT",
]

print("Languages: ")
for i in range(len(languages)):
    print(f"{i+1} - {languages[i]}")

language = int(input("Select a language: "))
language = languages[language - 1]


url = "https://api.themoviedb.org/3/movie/now_playing?language=" + language + "&page=1"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxYTJkMGQ0YmVjOWQ4NjFhMjFjMmJlMzAwZGI5NDk2NiIsInN1YiI6IjY0NjNjNmI2OGM0NGI5NzgwNzFmMzVhNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.LrT3myEXOkzgpq6nlHWLCEV0aOEsjfW0Bs342-Lu1ZQ",
}

response = requests.get(url, headers=headers)

print(response.text)
