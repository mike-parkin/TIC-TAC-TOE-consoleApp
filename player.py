import math
import random

class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass

# RandomComputer & Human inherits, functions from the class Player with the super() keyword
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # computer makes a random choice out of the list of availabel moves remaining
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            try:
                # check to see if input is an integer or in the list of available moves
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid Square. Try again')
        return val

# This player use the minimax algorithm
def GeniusComputerPlayer(Player): 
    def __init__(self, letter):
        super().__inti__(letter)
    
    def get_move(self, game):
        if len(game.available_moves() == 9):
            square = random.choice(game.available_moves())
        else:
            square = self.minimax(game, self.letter)
        return square

    def minimax(self, state, player):
        