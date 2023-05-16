import json


class Translator:
    def __init__(self, language):
        with open(f"locales/{language}.json", "r") as f:
            self.translations = json.load(f)

    def translate(self, key):
        return self.translations.get(key, f"No translation found for '{key}'")
