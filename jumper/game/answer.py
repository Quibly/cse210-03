import random
from game.guesser import guesser

class answer:

    def __init__(self):
        WORDS = ("python", "jumble", "easy", "difficult", "answer",  "thursday")
        self._word = random.choice(WORDS)
        self._guesser = guesser()
        self.answer_list = []
        self.word_list = []
        self._guessed_letters = []

    def get_word(self):
        return self._word    

    def _create_answer_list(self):
        self._answer_list.clear()
        for i in len(self.word):
            self.answer_list.append('_')

    def _append_guessed_letters_list(self):
        self._guessed_letters.append(self._guesser._letter_is)

    def _dispaly_answer_list(self):
        print(*self.answer_list)
            
    def _get_word_list(self):
        self.word_list = self._word.split('')

    def update_word_answer(self):
        for i in self.word_list:
            for j in self._guessed_letters:
                if i == j:
                    self.answer_list[i] = j


        
