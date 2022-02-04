from game.answer import answer
from game.guesser import guesser
from game.parachute import parachute


class director:
    """The main class of the game.

    This class oversees the organization of the gameplay.

    Attributes:
        
    
    """
    def __init__(self):
        """
        
        Args:
        """
        self._answer = answer()
        self._guesser = guesser()
        self._parachute = parachute()


    def start_game(self):
        """Method for structuring the order of events of game play
        """
        self._parachute._create_parachute()
        self._answer._create_answer_list()
        self._answer._get_word_list()
        while self._parachute._parachute_exists:
            self._get_answer()
            self._get_parachute()
            self._get_guesser()
            self._end_game()

    def _get_answer(self):
        """
        """
        self._answer._display_answer_list()

    def _get_parachute(self):
        """
        """
        if self._parachute._parachute_exists():
            if self._guesser._letter_in_word():
                self._parachute._display_parachute()
            else:
                self._parachute._break_parachute()
                self._parachute._display_parachute()
        
    def _get_guesser(self):
        """
        """
        self._guesser._get_letter()
        self._answer._append_guessed_letters_list()
        self._answer._update_answer_list()
    

    def _end_game(self):
        """Method for end game display
        """
        if not(self._parachute._parachute_exists()):
            print(f'\nYour parachute is gone. Your game is over.')

