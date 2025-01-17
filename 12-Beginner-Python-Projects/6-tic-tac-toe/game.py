# we need a board for tictactoe game. so we'll create a board here

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # we will use a single list to represent 3x3 board
        self.current_winner = None # To keep track of the winner!

    def print_board(self):   
        # This is just getting the rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc (tells us what number corresponding to what box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]         