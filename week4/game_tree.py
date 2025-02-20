class TicTacToe:

    def __init__(self):
        self.__board = []
        for _ in range(9):
            self.__board.append(' ')
        self.__running = True

    def display_board(self):
        # display the board as a 3 by 3 grid
        print(f"{self.__board[0]}_|_{self.__board[1]}_|_{self.__board[2]}")
        print(f"{self.__board[3]}_|_{self.__board[4]}_|_{self.__board[5]}")
        print(f"{self.__board[6]} | {self.__board[7]} | {self.__board[8]}")

    def player_move(self):
        position = (int(input("Enter your move (1-9): ")) - 1)
        # if position invalid, ask again
        if self.__board[position] != ' ':
            print("Position already occupied, please select again or press 0 to quit")
            position = (int(input("Enter your move (1-9): ")) - 1)
        elif position == -1:
            print("Thanks for playing, goodbye!")
            self.__running = False
        else:
            self.__board[position] = 'X'

    def game_over(self):
        pass

    def win(self):
        conditions = [0,1,2], [0,3,6], [0,4,8], [3,4,5], [1,4,7], [2,4,6], [6,7,8], [2,5,8]
        for condition in conditions:
            for i in condition:
                if self.__board[i] == 'X' or 'O':
                    return True
        else:
            return False

    def draw(self):
        pass

    def run(self):
        print("\n\nWelcome to Tic-Tac-Toe.\nYou are player X. I am player O.\n")
        while self.__running:
            self.display_board()
            self.player_move()

if __name__ == '__main__':
    game = TicTacToe()
    game.run()