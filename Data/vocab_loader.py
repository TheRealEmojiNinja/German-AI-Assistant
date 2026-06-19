import csv, Data.vocabulary as v

def loadVerbs(vocab_data : v.Vocabulary) -> None:
    with open('Data\\verbs.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            vocab_data.verbs[row["english"]] = row["german"]

def loadNouns(vocab_data : v.Vocabulary) -> None:
    with open('Data\\nouns.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            vocab_data.nouns[row["english"]] = [row["gender"], row["german"]]

def loadAdjectives(vocab_data : v.Vocabulary) -> None:
    with open('Data\\adjectives.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            vocab_data.adjectives[row["english"]] = row["german"]
            

