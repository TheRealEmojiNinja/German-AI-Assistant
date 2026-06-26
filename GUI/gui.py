import tkinter as tk, Systems.word_system as w, Data.vocabulary as v

class GermanAssistantInterface:

    question_text = "What is this {word} in German?"

    def __init__(self, root, vocab_data):

        self.current_word_type = ""

        self.top_frame = tk.Frame(root, borderwidth=5, relief="groove")
        self.bottom_frame = tk.Frame(root, borderwidth=5, relief="groove")

        self.top_frame.pack()
        self.bottom_frame.pack()

        self.start_label = tk.Label(self.top_frame, text="Welcome! Choose one of the buttons below: ", font=('Courier', 12, 'bold'))
        self.choose_verbs = tk.Button(self.top_frame, text="VERBS", command=lambda:self.question_verb(vocab_data), font=('Courier', 12, 'bold'), padx=20)
        self.choose_nouns = tk.Button(self.top_frame, text="NOUNS", command=lambda:self.question_noun(vocab_data), font=('Courier', 12, 'bold'), padx=20)
        self.choose_adjectives = tk.Button(self.top_frame, text="ADJECTIVES", command=lambda:self.question_adjective(vocab_data), font=('Courier', 12, 'bold'), padx=20)

        self.start_label.grid(row=0,column=0,columnspan=3)
        self.choose_verbs.grid(row=1,column=0)
        self.choose_nouns.grid(row=1,column=1)
        self.choose_adjectives.grid(row=1,column=2)

        self.question_label = tk.Label(self.bottom_frame, text="The question type will appear here.", font=('Courier', 12, 'bold'))
        self.word_label = tk.Label(self.bottom_frame, text="The word will appear here.", font=('Courier', 8))
        self.entry_box = tk.Entry(self.bottom_frame)
        self.result_label = tk.Label(self.bottom_frame, text='Your answer will be checked here!', font=('Courier', 12))
        self.submit_button = tk.Button(self.bottom_frame, text="Choose a word type!", state="disabled", command=lambda:self.verify_answer(vocab_data), font=('Courier', 14))

        self.question_label.pack()
        self.word_label.pack()
        self.entry_box.pack()
        self.result_label.pack()
        self.submit_button.pack()
    
    def verify_answer(self, vocab_data):
        if self.current_word_type == "verb":
            self.verify_verb_answer(vocab_data)
        elif self.current_word_type == "noun":
            self.verify_noun_answer(vocab_data)
        elif self.current_word_type == "adjective":
            self.verify_adjective_answer(vocab_data)
        
    def question_verb(self, vocab_data : v.Vocabulary):
        self.submit_button.config(text="SUBMIT", state="active")
        self.current_word_type = "verb"
        vocab_data.current_eng, vocab_data.current_ger = w.obtainVerb(vocab_data)
        self.question_label.config(text=GermanAssistantInterface.question_text.format(word="verb"))
        self.word_label.config(text=vocab_data.current_ger)

    def verify_verb_answer(self, vocab_data : v.Vocabulary):
        
        if self.entry_box.get().strip().lower() == vocab_data.current_eng.lower():
            vocab_data.current_eng, vocab_data.current_ger = w.obtainVerb(vocab_data)
            self.entry_box.config(text='')
            self.result_label.config(text='That\'s correct!')
            self.word_label.config(text=vocab_data.current_ger)
        else:
            self.result_label.config(text='That\'s incorrect!')

    def question_noun(self, vocab_data : v.Vocabulary):
        self.submit_button.config(text="SUBMIT", state="active")
        self.current_word_type = "noun"
        vocab_data.current_eng, vocab_data.current_ger = w.obtainNoun(vocab_data)
        self.question_label.config(text=GermanAssistantInterface.question_text.format(word="noun"))
        self.word_label.config(text=vocab_data.current_ger)

    def verify_noun_answer(self, vocab_data : v.Vocabulary):
        
        if self.entry_box.get().strip().lower() == vocab_data.current_eng.lower():
            vocab_data.current_eng, vocab_data.current_ger = w.obtainNoun(vocab_data)
            self.entry_box.config(text='')
            self.result_label.config(text='That\'s correct!')
            self.word_label.config(text=vocab_data.current_ger)
        else:
            self.result_label.config(text='That\'s incorrect!')

    def question_adjective(self, vocab_data : v.Vocabulary):
        self.submit_button.config(text="SUBMIT", state="active")
        self.current_word_type = "adjective"
        vocab_data.current_eng, vocab_data.current_ger = w.obtainAdjective(vocab_data)
        self.question_label.config(text=GermanAssistantInterface.question_text.format(word="adjective"))
        self.word_label.config(text=vocab_data.current_ger)

    def verify_adjective_answer(self, vocab_data : v.Vocabulary):
        
        if self.entry_box.get().strip().lower() == vocab_data.current_eng.lower():
            vocab_data.current_eng, vocab_data.current_ger = w.obtainAdjective(vocab_data)
            self.entry_box.config(text='')
            self.result_label.config(text='That\'s correct!')
            self.word_label.config(text=vocab_data.current_ger)
        else:
            self.result_label.config(text='That\'s incorrect!')
