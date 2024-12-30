from piece import Piece
from position import Position

class Pawn(Piece):
    def __init__(self, color=0, position=Position(0, 0)):
        super().__init__(color, position)
        self.row = self.position.row
        self.column = self.position.column
        self.has_moved = False
        
        if color == 0:
            self.image = '/assets/white_pawn.png'
        else:
            self.image = '/assets/black_pawn.png'
            
    def is_valid_move(self, new_position, board):
        direction = 1 if self.color == 0 else -1
        start_row = 1 if self.color == 0 else 6

        if new_position.column == self.position.column:
            if new_position.row == self.position.row + direction:
                return board.board[new_position.row][new_position.column] is None
            elif new_position.row == self.position.row + 2 * direction and self.position.row == start_row:
                intermediate_row = self.position.row + direction
                
                return (board.board[new_position.row][new_position.column] is None and
                        board.board[intermediate_row][new_position.column] is None)

        if abs(new_position.column - self.position.column) == 1:
            if new_position.row == self.position.row + direction:
                target_piece = board.board[new_position.row][new_position.column]
                if target_piece is not None and target_piece.color != self.color:
                    return True
                if self.position.row == (3 if self.color == 0 else 4):
                    adjacent_pawn = board.board[self.position.row][new_position.column]
                    if isinstance(adjacent_pawn, Pawn) and adjacent_pawn.color != self.color and adjacent_pawn.en_passant:
                        return True

        return False

    def promote(self, new_piece_type):
        if (self.color == 0 and self.position.row == 7) or (self.color == 1 and self.position.row == 0):
            return new_piece_type(self.color, self.position)
        return self
