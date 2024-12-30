from piece import Piece
from position import Position

class Knight(Piece):
    def __init__(self, color=0, position=Position(0, 0)):
        super().__init__(color, position)
        self.row = self.position.row
        self.column = self.position.column
        self.has_moved = False
        
        if color == 0:
            self.image = '/assets/white_knight.png'
        else:
            self.image = '/assets/black_knight.png'
            
    def is_valid_move(self, new_position=Position(0, 0), board=None):
        new_position_piece = board.board[new_position.row][new_position.column]
        
        if new_position_piece is not None and new_position_piece.color == self.color:
            return False
        
        delta_x = new_position.row - self.position.row
        delta_y = new_position.column - self.position.column
        
        if (abs(delta_x) == 1 and abs(delta_y) == 2) or (abs(delta_x) == 2 and abs(delta_y) == 1):
            return True
        
        return False
              
    def possible_moves(self, board=None):
        possible_moves = []
        for i in range(0, 8):
            for j in range(0, 8):
                new_position = Position(i, j)

                if new_position != self.position:
                    if self.is_valid_move(new_position, board):
                        possible_moves.append(new_position)
                        
        return possible_moves
