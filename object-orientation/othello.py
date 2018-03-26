class Game(object):
    colors = ["black", "white"]

    def __init__(self):
        self.board = Board()

        self.curr_color = "black"
        self.other_color = "white"

    def play(self):
        self.board.show_board()
        if self.curr_color == "black":
            print "Your turn black"
        else:
            print "Your turn white"

        col, row = self._get_user_move()
        self.board.board[row][col].update_square(self.curr_color)

        while not self.board.move(self.curr_color, self.other_color, row, col):
            col, row = self._get_user_move()

        self.curr_color, self.other_color = self.other_color, self.curr_color

    def _get_user_move(self):

        col, row = map(lambda(num): int(num), raw_input("enter axis as x, y:").split(", "))

        while not self.board.check_valid_move(col, row):
            col, row = map(lambda(num): int(num), raw_input("enter axis as x, y:").split(", "))

        return (col, row)

class Board(object):

    def __init__(self):
        """ Create a board with the current starting pieces in place"""

        self.board = []
        for i in range(8):
            row = []
            for j in range(8):
                row.append(Square())
            self.board.append(row)
        self.board[3][3].occupied = "white"
        self.board[3][4].occupied = "black"
        self.board[4][4].occupied = "white"
        self.board[4][3].occupied = "black"
        print "Board:"
        self.show_board()

        self.black = 0
        self.white = 0

    def show_board(self):
        """ Display current status of board"""

        print "     ", "   |   ".join([str(i) for i in range(8)])
        for i in range(8):
            print  i, "|", " | ".join([col.occupied if col.occupied else"-----" for col in self.board[i]])

    def check_valid_move(self, row, col):
        """ Is the move on the board and not in a currently occupied spot"""

        if row < 0 or col < 0 or row > 7 or col > 7:
            print "Entry is not on the board"
            return False
        if self.board[row][col].occupied:
            print "That space is already taken"
            return False
        return True

    def move(self, curr_color, other_color, row, col):

        valid_move_row = self._make_row_flips(curr_color, other_color, row, col)
        valid_move_col = self._make_col_flips(curr_color, other_color, row, col)

        if not valid_move_col and not valid_move_row:
            print "Not a valid move"
            return False
        return True

    def _make_row_flips(self, curr_color, other_color, row, col):
        """ Find changable pieces and return whether any changes were made"""

        changed = False
        start = 0
        end = col + 1

        while end < 8 and self.board[row][end].occupied == other_color:
            changed = True
            self.board[row][end].update_square(curr_color)
            end += 1

        end = col - 1
        while end > 0 and self.board[row][end].occupied == other_color:
            changed = True
            self.board[row][end].update_square(curr_color)
            end -= 1

        return changed

    def _make_col_flips(self, curr_color, other_color, row, col):

        changed = False

        for i in range(row + 1, 8):
            print i
            if self.board[i][col].occupied == curr_color:
                changed = True
                for j in range(row, i):
                    self.board[j][col].update_square(curr_color)
                break
        for i in range(row - 1, 0, -1):
            if self.board[i][col].occupied == curr_color:
                changed = True
                for j in range(row, i, -1):
                    self.board[j][col].update_square(curr_color)
                break
        return changed

class Square(object):

    def __init__(self):
        self.occupied = False

    def __repr__(self):
        return str(self.occupied)

    def update_square(self, color):
        self.occupied = color
