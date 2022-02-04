import random

class answer:
    """
    The answer class handles methods for answer display and answer verifications
    """

    def __init__(self):
        """
        Attributes:
        self._words holds a list of possible words for an answer key
        self._word holds the word that is the answer solution
        self._answer_list holds a list of letters and '_' characters for displaying the current status of guesses
        self._word_list holds a list of letters that make up the word being guessed at
        self._guessed_letters holds a list of letters that have already beeen guessed
        """
        self._words = ("python", "jumble", "easy", "difficult", "answer",  "thursday")
        self._word = ''
        self._answer_list = []
        self._word_list = []
        self._guessed_letters = []

    def _get_word(self):
        """
        This method returns the value of the word being guessed at.
        """
        return self._word    

    def _create_answer_list(self):
        """
        This method chooses a random word from the words list, places it in the self._word variable for storage
        and creates an _answer_list list that is used to display the current progress of guesses
        """
        self._word = random.choice(self._words)
        for i in range(len(self._word)):
            self._answer_list.append('_')

    def _append_guessed_letters_list(self, letter):
        """
        This method appends the guessed letters list with the current guess.
        This is used to keep track of what has been guessed already.
        """
        self._guessed_letters.append(letter)

    def _display_answer_list(self):
        """
        This method displays the current guessing progress from the answer list.
        """
        print(*self._answer_list)
        print()
            
    def _get_word_list(self):
        """
        This method creates a list of characters that make up the word being guessed at.
        """
        self._word_list = list(self._word)

    def _update_answer_list(self):
        """
        This method loops through the letters of the word being guessed at and changes the
        answer list to reflect correct answers.
        """
        for i in range(len(self._word_list)):
            for j in range(len(self._guessed_letters)):
                if self._word_list[i] == self._guessed_letters[j]:
                    self._answer_list[i] = self._guessed_letters[j]


    def _check_for_win(self):
        """
        This method checks to see if the player has one based on their current guess.
        It loops through the answer list and checks to see if all the letters have been guessed correctly.
        """
        counter = 0
        for i in range(len(self._answer_list)):
            if self._answer_list[i] == '_':
                counter += 1
        if counter == 0:
            return True
        else:
            return False

    def _current_list_of_guesses(self):
        """
        This method displays a list of the current guesses.
        """
        print(f'\nGuessed letters: ')
        print(*self._guessed_letters)
        print()
