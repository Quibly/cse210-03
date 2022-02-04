from game.answer import answer
from game.guesser import guesser
from game.parachute import parachute


class director:
    """The main class of the game.

    This class oversees the organization of the gameplay.
    """
    def __init__(self):
        """
        Args:
        self._answer connects diretor to 'answer' class object methods
        self._guesser connects diretor to 'guesser' class object methods
        self._parachute connects diretor to 'parachute' class object methods
        self._gameover is a variable for determining if the game is over

        """
        self._answer = answer()
        self._guesser = guesser()
        self._parachute = parachute()
        self._gameover = False


    def start_game(self):
        """
        Method for structuring the order of events of game play
        The method creates the parachute list for display, creates an answer list for answer status display,
        and initiates the creation of a list of the letters in the word being guessed at.

        After creating the basic lists and variables needed for the program to run
        the method then cycles through instances of guesses and gameplay until the game is over.
        """
        self._parachute._create_parachute()
        self._answer._create_answer_list()
        self._answer._get_word_list()
        while self._parachute._parachute_exists and self._gameover == False:
            self._get_answer()
            self._get_parachute()
            self._get_guesser()
            self._end_game()

    def _get_answer(self):
        """
        This method displays the current solution status of the game.
        """
        if self._parachute._parachute_exists():
            self._answer._display_answer_list()

    def _get_parachute(self):
        """
        This method determines if the guess was correct and displays the new 
        status of the parachute based on what was guessed.
        """
        if self._parachute._parachute_exists():
            word = self._answer._get_word()
            if self._guesser._letter_in_word(word):
                self._parachute._display_parachute()
            else:
                self._parachute._break_parachute()
                self._parachute._display_parachute()
        
    def _get_guesser(self):
        """
        This method updates the answer results based on the current guess.
        """
        if self._parachute._parachute_exists():
            self._guesser._get_letter()
            letter = self._guesser._letter_is()
            self._answer._append_guessed_letters_list(letter)
            self._answer._update_answer_list()
    

    def _end_game(self):
        """
        Method for end game display.
        It checks to see if the game is over whether it is caused by the parachute being depleted
        or by the correct answer being completed.
        """
        if not(self._parachute._parachute_exists()):
            print(f'\nYour parachute is gone. Your game is over.')
            self._gameover=True
        if self._answer._check_for_win():
            print('You Won!')
            self._gameover=True


