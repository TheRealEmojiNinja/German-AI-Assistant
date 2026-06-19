import Data.vocabulary as v, Data.vocab_loader as vl

vocab = v.Vocabulary()
vl.loadVerbs(vocab)
vl.loadNouns(vocab)
vl.loadAdjectives(vocab)


print("verbs", vocab.verbs, "\nnouns", vocab.nouns, "\nadjectives", vocab.adjectives)