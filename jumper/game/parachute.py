
class parachute:
    """This class handles the display and parachute condition tracking.

    Attributes:
    
    """

    def __init__(self):
        """
        Arguments:
        self._parachute holds the current status of our parachute display
        """
        self._parachute = []


    def create_parachute(self):
        """
        This method hols a list of the layers for the parachute display. The list values each hold a single line of the parachute.
        """
        self._parachute = [' \\ / ', '\\   /', '/___\\',  ' ___ ', 'garbage']

    
    def display_parachute(self):
        """
        This method loops through the active layers of the parachute and displays what is remaining in the list.
        """
        for i in range(len(self._parachute)-1, -1, -1):
            print(f' {self._parachute[i]}')
        print('   O  \n  /|\\ \n  / \\ ')
        print('\n^^^^^^^\n')

    def break_parachute(self):
        """
        This method removes a value in the parachute list.
        """
        self._parachute.pop()

    def parachute_exists(self):
        """
        This method checks to see if there are any values remaining in the parachute list.
        """
        return (len(self._parachute) != 0)