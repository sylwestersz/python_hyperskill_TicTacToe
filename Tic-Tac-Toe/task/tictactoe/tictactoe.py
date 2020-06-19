import sys


class TicTacToe:

    WIN_INDEXES = [[0, 1, 2], [3, 4, 5],
                   [6, 7, 8], [0, 3, 6],
                   [1, 4, 7], [2, 5, 8],
                   [0, 4, 8], [2, 4, 6]]
    CLEAN_BOARD = " "*9

    def __init__(self, player):
        self.current_player = player
        self.winner = None
        self.field_int = [0, 0]
        self.allowed_fields = [1, 2, 3]
        self.board = [[elem for elem in TicTacToe.CLEAN_BOARD[6:9]],
                      [elem for elem in TicTacToe.CLEAN_BOARD[3:6]],
                      [elem for elem in TicTacToe.CLEAN_BOARD[0:3]]]

    def determine_winner(self):
        sequence = [item for sublist in self.board for item in sublist]
        for i in range(len(TicTacToe.WIN_INDEXES)):
            if ''.join([sequence[k] for k in TicTacToe.WIN_INDEXES[i]]) == 'XXX':
                self.winner = "X"
            if ''.join([sequence[k] for k in TicTacToe.WIN_INDEXES[i]]) == 'OOO':
                self.winner = "O"

    def is_finished(self):
        sequence = [item for sublist in self.board for item in sublist]
        if " " not in sequence or self.winner is not None:
            return True
        return False

    def print_result(self):
        if self.winner is None:
            print("Draw")
        else:
            print(f"{self.winner} wins")

    def print_current_field(self):
        print("---------")
        print("|", " ".join(self.board[2]), "|")
        print("|", " ".join(self.board[1]), "|")
        print("|", " ".join(self.board[0]), "|")
        print("---------")

    def coordinates_ok(self, field):
        if not (field[0].isdecimal() and field[1].isdecimal()):
            print("You should enter numbers!")
            return False
        self.field_int = [int(value) for value in field]
        if self.field_int[0] not in self.allowed_fields or self.field_int[1] not in self.allowed_fields:
            print("Coordinates should be from 1 to 3!")
            return False
        if self.board[self.field_int[1] - 1][self.field_int[0] - 1] != " ":
            print("This cell is occupied! Choose another one!")
            return False
        return True

    def add_element(self):
        self.board[self.field_int[1] - 1][self.field_int[0] - 1] = self.current_player

    def change_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        elif self.current_player == "O":
            self.current_player = "X"
        else:
            print("Internal ERROR, unknown player, aborting")
            sys.exit()


starting_player = "X"
game = TicTacToe(starting_player)

while True:
    game.print_current_field()
    print("Enter the coordinates:")
    field_str = input().split()
    if game.coordinates_ok(field_str):
        game.add_element()
        game.change_player()
        game.determine_winner()
        if game.is_finished():
            game.print_current_field()
            game.print_result()
            sys.exit()
