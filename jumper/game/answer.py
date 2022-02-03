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

    def answer_display(self, word):
        word_count = len(word)
        for i in range(word_count):
            print("_ ", sep=' ', end='', flush=True)

        
