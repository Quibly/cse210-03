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
        self._current_guess = ''
        self._guesser = guesser()
        self._parachute = parachute()


    def start_game(self):
        """Method for structuring the order of events of game play
        """
        self._parachute._create_parachute()
        while self._parachute._parachute_exists:
            self._get_answer()
            self._get_parachute()
            self._get_guesser()
            self._end_game()

    def _get_answer(self):
        """
        """
        pass

    def _get_parachute(self):
        """
        """
        if self._parachute._parachute_exists:
            self._parachute._display_parachute




    def _get_guesser(self):
        """
        """
        pass
    

    def _end_game(self):
        """Method for end game display
        """
        if not(self._parachute._parachute_exists()):
            print(f'\nYour parachute is gone. Your game is over.')

