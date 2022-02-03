from game.director import director

class parachute:
    """This class handles the display and parachute condition tracking.

    Attributes:
    
    """

    def __init__(self):
        """
        
        Args:
        """
        self._parachute = []
        self._parachute_exists = True


    def _create_parachute(self):
        """
        """
        self._parachute = [' / \\ ', ' /|\\ ', '  O  ', ' \\ / ', '\\   /', '/___\\', ' ___ ']

    
    def _display_parachute(self):
        """
        """
        for i in range(len(self._parachute), 0, -1):
            print(f' {self._parachute[i]}')

        print('\n^^^^^^^\n')

    def _break_parachute(self):
        """
        """
        self._parachute.pop()

    def _parachute_exists(self):
        """
        """
        return not(self._parachute)