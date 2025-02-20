class TicTacToe:

    def __init__(self):
        self.__board = [' ' for _ in range(9)]
        self.__running = True

    def display_board(self):
        # display the board as a 3 by 3 grid
        print(f"\n{self.__board[0][1][2]}")
        print(f"\n{self.__board[3][4][5]}")
        print(f"\n{self.__board[6][7][8]}")

    def player_move(self):
        position = (int(input("Enter your move (1-9): ")) - 1)
        # if position invalid, ask again
        if self.__board[position] != ' ':
            print("Position already occupied, please select again or press q to quit")
            position = (int(input("Enter your move (1-9): ")) - 1)
        elif position == 'q':
            print("Thanks for playing, goodbye!")
            self.__running = False
        else:
            self.__board[position] = 'X'

    def run(self):
        print("Welcome to Tic-Tac-Toe.\nYou are player X. I am player O.\n")
        while self.__running:
            self.display_board()
            self.player_move()

if __name__ == '__main__':
    game = TicTacToe()
    game.run()