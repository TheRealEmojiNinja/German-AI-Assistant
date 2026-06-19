import tkinter as tk, Systems.verb_system as verb

class GermanAssistantInterface:
    def __init__(self, root, vocab_data):
        self.question_label = tk.Label(root, text="What is this verb in German?", font=('Courier', 12, 'bold'))
        self.verb_eng, self.verb_ger = verb.obtainVerb(vocab_data) 
        self.verb_label = tk.Label(root, text=self.verb_eng, font=('Courier', 8))
        self.verb_entry = tk.Entry(root)
        tk.Button(root, text="Submit Answer", command=self.verify_answer(vocab_data)).pack()
        self.result_label = tk.Label(root, text='Your answer will be checked here!')

        self.question_label.pack()
        self.verb_label.pack()
        self.verb_entry.pack()
        self.result_label.pack()
    
    def verify_answer(self, vocab_data):
        print('function called')
        if self.verb_entry.get().strip().lower() == self.verb_ger.lower():
            self.verb_eng, self.verb_ger = verb.obtainVerb(vocab_data) 
            self.verb_entry.config(text='')
            self.result_label.config(text='That\'s correct!')
            self.verb_label.config(text=self.verb_eng)
        else:
            #self.result_label.config(text='That\'s incorrect!')
            pass