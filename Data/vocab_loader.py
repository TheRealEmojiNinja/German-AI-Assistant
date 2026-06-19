import csv, Data.vocabulary as v

def loadVerbs(vocab_data : v.Vocabulary) -> None:
    with open('German AI Assistant\Data\\verbs.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            vocab_data.verbs[row["german"]] = row["english"]
            

