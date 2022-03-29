import json


def load_file():
    with open("candidates.json", encoding="utf-8") as file:
        data = json.load(file)
        candidates = {}
        for item in data:
            candidates[item["id"]] = item
    return candidates
