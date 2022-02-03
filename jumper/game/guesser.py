from game.answer import answer

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
        self._answer = answer()

    def _get_letter(self):
        """
        """
        self.guess = input("\nPlease guess a letter [a-z]: ")

    def _letter_is(self):
        """
        """
        return self.guess

    def _letter_in_word(self):
        """
        """
        self._answer.get_word()
        return (self.guess in self._answer.get_word.split(''))
