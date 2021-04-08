class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        moves = []
        for (i, x) in enumerate(self.board):
            # x is the 'square' of the board
            if x == ' ':
                moves.append(i)
        return moves
        # return[i for i, spot in enumerate(self.board) if spot == ' ']
        # ^^^ this line will return the same results as the for loop
    
    def empty_squares(self):


def play(game, x_player, o_player, print_game = True):
    if print_game:
        game.print_board_nums()
    #starting move goes to 'X'    
    letter = 'X'
    # itertate through the empty squares


