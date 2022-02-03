import random
from game.guesser import guesser

class answer:


    def __init__(self):
        WORDS = ("python", "jumble", "easy", "difficult", "answer",  "thursday")
        self._word = random.choice(WORDS)
        self._guesser = guesser()

    def get_word(self):
        return self._word

    def move_word(self, word):
        self._word = word

    def get_word_count(self, word):
        word_count = "_ " * len(word)
        print(word_count)
        print(word)

    def answer_display(self, word, ):
        guessed = False
        while not guessed:
            word_as_list = list(word_count)
            indices = [i for i, letter in enumerate(word) if letter == self._guesser._letter_is()]
            for index in indices:
                word_as_list[index] = self._guesser._letter_is()
                word_count = "".join(word_as_list)
            if "_" not in word_count:
                guessed = True
            print(word_count)
        

        
