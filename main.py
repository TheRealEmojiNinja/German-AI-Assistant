import Data.vocabulary as v, Data.vocab_loader as vl, Systems.verb_system as verb

vocab = v.Vocabulary()
vl.loadVerbs(vocab)
vl.loadNouns(vocab)
vl.loadAdjectives(vocab)

print(verb.obtainVerb(vocab))

running = False

while running:
    pass