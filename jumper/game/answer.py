import random
from guesser import guesser

class answer:

    def __init__(self):
        WORDS = ("python", "jumble", "easy", "difficult", "answer",  "thursday")
        self._word = random.choice(WORDS)

    def get_word(self):
        return self._word

    def move_word(self, word):
        self._word = word

    def answer_display(self, word, new_letter):
        word_count = "_" * len(word)
        print(word_count)
        

        
