import Data.vocabulary as v, Data.vocab_loader as vl, GUI.gui as interface
import tkinter as tk

vocab = v.Vocabulary()
vl.loadVerbs(vocab)
vl.loadNouns(vocab)
vl.loadAdjectives(vocab)

running = True

root = tk.Tk()
root.geometry("600x600")

screen = interface.GermanAssistantInterface(root, vocab)

root.mainloop()

