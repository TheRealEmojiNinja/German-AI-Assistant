import Data.vocabulary as v, Data.vocab_loader as vl, Systems.verb_system as verb, GUI.gui as interface
import tkinter as tk

vocab = v.Vocabulary()
vl.loadVerbs(vocab)
vl.loadNouns(vocab)
vl.loadAdjectives(vocab)

running = True

root = tk.Tk()
root.geometry("600x600")

vocab.current_eng, vocab.current_ger = verb.obtainVerb(vocab) 

def verify_answer(vocab_data : v.Vocabulary, result_label : tk.Label):
        if verb_entry.get().strip().lower() == vocab_data.current_ger.lower():
            vocab.current_eng, vocab.current_ger = verb.obtainVerb(vocab) 
            verb_entry.delete(0, tk.END)
            result_label.config(text='That\'s correct!')
            verb_label.config(text=vocab.current_eng)
        else:
            result_label.config(text='That\'s incorrect!')


question_label = tk.Label(root, text="What is this verb in German?", font=('Courier', 12, 'bold'))
verb_label = tk.Label(root, text=vocab.current_eng, font=('Courier', 8))
verb_entry = tk.Entry(root)
result_label = tk.Label(root, text='Your answer will be checked here!')
submit_button = tk.Button(root, text="Submit Answer", command=lambda: verify_answer(vocab, result_label))

question_label.pack()
verb_label.pack()
verb_entry.pack()
result_label.pack()
submit_button.pack()

#screen = interface.GermanAssistantInterface(root, vocab)

root.mainloop()

