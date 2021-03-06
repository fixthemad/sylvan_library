import json

from data_import.staging import *
from data_import import _paths


class JsonImporter:
    def __init__(self):
        self.sets = list()
        pass

    def parse_json(self):
        f = open(_paths.json_data_path, 'r', encoding="utf8")
        json_data = json.load(f, encoding='UTF-8')
        f.close()
        return json_data

    def import_data(self):
        json_data = self.parse_json()

        raw_sets = sorted(
            json_data.items(),
            key=lambda card_set: card_set[1]["releaseDate"])

        for raw_set in raw_sets:
            self.add_set(raw_set[1])

    def add_set(self, json_set):
        s = StagedSet(json_set)
        self.sets.append(s)

    def get_staged_sets(self):
        return self.sets

    def import_colours(self):
        file = open(_paths.colour_json_path, 'r', encoding='utf8')
        colours = json.load(file, encoding='UTF-8')
        file.close()

        return colours

    def import_rarities(self):
        file = open(_paths.rarity_json_path, 'r', encoding="utf8")
        rarities = json.load(file, encoding='UTF-8')
        file.close()

        return rarities

    def import_languages(self):
        f = open(_paths.language_json_path, 'r', encoding="utf8")
        languages = json.load(f, encoding='UTF-8')
        f.close()

        return languages
