import json


def init_words(file_to_open, file_to_write):
    words = {}
    with open(file_to_open, "r") as file:
        for line in file:
            word = line.strip()
            if len(word) in words:
                words[len(word)].append(word)
            else:
                words[len(word)] = [word]
    sorted_words = dict(sorted(words.items()))
    with open(file_to_write, "w") as file:
        json.dump(sorted_words, file)
