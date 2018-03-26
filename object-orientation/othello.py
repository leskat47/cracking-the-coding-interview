class Game(object):
    colors = ["black", "white"]

    def __init__(self):
        self.board = []
        for i in range(8):
            row = []
            for j in range(8):
                row.append(Square())
            self.board.append(row)
        self.board[3][3].occupied = "white"
        self.board[3][4].occupied = "black"
        self.board[4][4].occupied ="white"
        self.board[4][3].occupied = "black"
        print "Board:"
        self.show_board()

        self.black = 0
        self.white = 0

        self.curr_color = "black"
        self.other_color = "white"

    def show_board(self):
        print "     ", "   |   ".join([str(i) for i in range(8)])
        for i in range(8):
            print  i, "|", " | ".join([col.occupied if col.occupied else"-----" for col in self.board[i]])


class Square(object):

    def __init__(self):
        self.occupied = False

    def __repr__(self):
        return str(self.occupied)
