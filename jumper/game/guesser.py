

class guesser:

    """
    Class for getting input from the user and checking whether the guess is found
    in the answer.

    Attributes

    """
    def __init__(self):
        """
        """
        self._guess = ''
        self._word_list = []

    def _get_letter(self):
        """
        """
        self._guess = input("\nPlease guess a letter [a-z]: ")

    def _letter_is(self):
        """
        """
        return self._guess

    def _letter_in_word(self, word):
        """
        """
        self._word_list = list(word)
        return (self._guess in self._word_list)
