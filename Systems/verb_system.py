import Data.vocabulary as v, random

def obtainVerb(vocab_data : v.Vocabulary) -> tuple[str, str]:
    word_eng : str = random.choice(list(vocab_data.verbs.keys()))
    word_ger : str = vocab_data.verbs[word_eng]
    return (word_eng, word_ger)
