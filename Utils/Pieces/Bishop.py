from Utils.Piece import Piece


class Bishop(Piece):
    def __init__(self, position, color):
        super().__init__(position)
        self.color = color
        self.type = "Bishop"
        self.photo = "images/wB.png" if color == "white" else "images/bB.png"

    def bishop_can_move(self, board):
        output = ((-1, -1), (1, 1), (1, -1), (-1, 1))
        return self.create_moves(board,output)

    def get_type(self):
        return self.type

    def get_identificator(self):
        return self.color[0] + 'B'
