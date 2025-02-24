class TicTacToe:

    def __init__(self):
        self.__board = [' '] * 9
        self.__running = True

    def display_board(self):
        print(f"{self.__board[0]}_|_{self.__board[1]}_|_{self.__board[2]}")
        print(f"{self.__board[3]}_|_{self.__board[4]}_|_{self.__board[5]}")
        print(f"{self.__board[6]} | {self.__board[7]} | {self.__board[8]}")

    def minimax(self, is_max: bool) -> int:
        # Base Cases
        if self.win('O'): return 1   # AI wins
        if self.win('X'): return -1  # Player wins
        if self.draw(): return 0     # Draw

        if is_max:  # AI (O) is maximizing
            best_score = float('-inf')
            for i in range(9):
                if self.__board[i] == ' ':
                    self.__board[i] = 'O'
                    score = self.minimax(False)
                    self.__board[i] = ' '
                    best_score = max(score, best_score)
            return best_score
        else:  # Player (X) is minimizing
            best_score = float('inf')
            for i in range(9):
                if self.__board[i] == ' ':
                    self.__board[i] = 'X'
                    score = self.minimax(True)
                    self.__board[i] = ' '
                    best_score = min(score, best_score)
            return best_score

    def player_move(self):
        while True:
            try:
                position = int(input("Enter your move (1-9): ")) - 1
                if position == -1:
                    print("Thanks for playing, goodbye!")
                    self.__running = False
                    return
                if 0 <= position <= 8 and self.__board[position] == ' ':
                    self.__board[position] = 'X'
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Please enter a number between 1 and 9.")

    def computer_move(self):
        best_move = None
        best_score = float('-inf')  # Now maximizing for AI

        for i in range(9):
            if self.__board[i] == ' ':
                self.__board[i] = 'O'
                score = self.minimax(False)
                self.__board[i] = ' '
                if score > best_score:
                    best_score = score
                    best_move = i

        if best_move is not None:
            self.__board[best_move] = 'O'

    def game_over(self, player):
        if self.win(player):
            self.display_board()
            print(f"{'You' if player == 'X' else 'I'} win!")
            return True

        if self.draw():
            self.display_board()
            print("It's a draw!")
            return True

        return False

    def win(self, player: str):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        return any(all(self.__board[cell] == player for cell in condition) for condition in win_conditions)

    def draw(self):
        return ' ' not in self.__board

    def run(self):
        print("\n\nWelcome to Tic-Tac-Toe.\nYou are player X. I am player O.\n")
        while self.__running:
            self.display_board()
            self.player_move()
            if not self.__running or self.game_over('X'):
                break
            self.computer_move()
            if self.game_over('O'):
                break

if __name__ == '__main__':
    game = TicTacToe()
    game.run()
