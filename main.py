import Data.vocabulary as v, Data.vocab_loader as vl

vocab = v.Vocabulary()
vl.loadVerbs(vocab)


print(vocab.verbs)