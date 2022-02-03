import random
from guesser import guesser

class answer:


    def __init__(self):
        WORDS = ("python", "jumble", "easy", "difficult", "answer",  "thursday")
        self._word = random.choice(WORDS)

    def get_word(self):
        return self._word

    def move_word(self, word):
        self._word = word

    def answer_display(self, word, new_letter):
        guessed = False
        while not guessed:
            word_count = "_ " * len(word)
            print(word_count)
            print(word)
            guess = input("Please guess a letter or word: ")
            word_as_list = list(word_count)
            indices = [i for i, letter in enumerate(word) if letter == guess]
            for index in indices:
                word_as_list[index] = guess
                word_count = "".join(word_as_list)
                if "_" not in word_count:
                    guessed = True
    

        print(word_count)
        

        
