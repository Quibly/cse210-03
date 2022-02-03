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

    

    def _get_answer_list(self):
        self._answer_list.clear()
        for i in len(self.word):
            self.answer_list.append('_')

    def _get_word_list(self):
        self.word_list = self._word.split('')

    def display_word_answer(self):
        for i in self.word_list:
            for j in self._guessed_letters:
                if i == j:
                    self.answer_list[i] = j


        
