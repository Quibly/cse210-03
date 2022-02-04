

class parachute:
    """This class handles the display and parachute condition tracking.

    Attributes:
    
    """

    def __init__(self):
        """
        
        Args:
        """
        self._parachute = []


    def _create_parachute(self):
        """
        """
        self._parachute = [' / \\ ', ' /|\\ ', '  O  ', ' \\ / ', '\\   /', '/___\\', ' ___ ', 'garbage']

    
    def _display_parachute(self):
        """
        """
        for i in range(len(self._parachute)-1, -1, -1):
            print(f' {self._parachute[i]}')

        print('\n^^^^^^^\n')

    def _break_parachute(self):
        """
        """
        self._parachute.pop()

    def _parachute_exists(self):
        """
        """

        return (len(self._parachute) != 0)