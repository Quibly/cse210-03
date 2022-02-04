import random

class answer:

    def __init__(self):
        self._words = ("python", "jumble", "easy", "difficult", "answer",  "thursday")
        self._word = ''
        self._answer_list = []
        self._word_list = []
        self._guessed_letters = []

    def _get_word(self):
        return self._word    

    def _create_answer_list(self):
        self._answer_list.clear()
        self._word = random.choice(self._words)
        for i in range(len(self._word)):
            self._answer_list.append('_')

    def _append_guessed_letters_list(self, letter):
        self._guessed_letters.append(letter)

    def _display_answer_list(self):
        print(*self._answer_list)
        print()
            
    def _get_word_list(self):
        self._word_list = self._word.split()

    def _update_answer_list(self):
        for i in self._word_list:
            for j in self._guessed_letters:
                if i == j:
                    self._answer_list[i] = j


        
