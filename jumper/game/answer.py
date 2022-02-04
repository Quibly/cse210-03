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
        self._word = random.choice(self._words)
        for i in range(len(self._word)):
            self._answer_list.append('_')
        print(self._answer_list)

    def _append_guessed_letters_list(self, letter):
        self._guessed_letters.append(letter)
        print(self._guessed_letters)

    def _display_answer_list(self):
        print(*self._answer_list)
        print()
            
    def _get_word_list(self):
        self._word_list = list(self._word)
        print(self._word_list)

    def _update_answer_list(self):
        for i in range(len(self._word_list)):
            for j in range(len(self._guessed_letters)):
                if self._word_list[i] == self._guessed_letters[j]:
                    self._answer_list[i] = self._guessed_letters[j]
        print(self._answer_list)


    def _check_for_win(self):
        counter = 0
        for i in range(len(self._answer_list)):
            if self._answer_list[i] == '_':
                counter += 1
        if counter == 0:
            return True
        else:
            return False

