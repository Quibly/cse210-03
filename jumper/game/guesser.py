

class guesser:

    """
    Class for getting input from the user and checking whether the guess is found
    in the answer.
    """
    def __init__(self):
        """
        Attributes:
        self._guess holds the value of the current guess
        self._word_list holds a list of all the characters in the word being guessed at
        """
        self._guess = ''
        self._word_list = []

    def get_letter(self):
        """
        This method gets input from the user on which letter they want to guess and
        places the input into a variable for storing the guess.
        """
        self._guess = input("\nPlease guess a letter [a-z]: ")

    def letter_is(self):
        """
        This method returns the value of the current guess.
        """
        return self._guess

    def letter_in_word(self, word):
        """
        This method checks to see if the current guess is found in the word being guessed at.
        """
        self._word_list = list(word)
        return (self._guess in self._word_list)
