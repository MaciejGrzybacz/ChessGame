class Piece:
    def __init__(self, position):
        self.position = position
        self.has_moved = False
        self.picture = None

    # Getters
    def get_position(self):
        return self.position

    def get_picture(self):
        return self.picture

    # Setter
    def move(self, new_position):
        self.position = new_position
        self.has_moved = True

    def create_moves(self, board):
        moves = []
        attack_moves = []
        x, y = self.position
        output = []

        for move in output:
            new_x = x + move[0]
            new_y = y + move[1]
            while 8 > new_x >= 0 and new_y < 8 and new_y >= 0 and board[new_y][new_x] is None:
                moves.append((new_x, new_y))
                new_x += move[0]
                new_y += move[1]

            if 8 > new_x >= 0 and new_y < 8 and new_y >= 0 and board[new_y][new_x] is not None and \
                    board[new_y][new_x].color != self.color:
                attack_moves.append((new_x, new_y))

        return moves, attack_moves
