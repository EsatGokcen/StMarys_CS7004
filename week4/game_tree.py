class TicTacToe:

    def __init__(self):
        self.__board = [' ' for _ in range(9)]

    def display_board(self):
        pass
        #display the board as a 3 by 3 grid

    def player_move(self):
        position = (int(input("Enter your move (1-9): ")) - 1)
        # if position invalid, ask again
        self.__board[position] = 'X'

    def run(self):
        print("Welcome to Tic-Tac-Toe.\nYou are player X. I am player O.\n")
        while True:
            self.display_board()
            self.player_move()

if __name__ == '__main__':
    game = TicTacToe()
    game.run()