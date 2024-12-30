from piece import Piece
from position import Position

class Queen(Piece):
    def __init__(self, color=0, position=Position(0, 0)):
        super().__init__(color, position)
        self.row = self.position.row
        self.column = self.position.column
        self.has_moved = False
        
        if color == 0:
            self.image = '/assets/white_queen.png'
        else:
            self.image = '/assets/black_queen.png'
            
    def is_valid_move(self, new_position=Position(0, 0), board=None):
        new_position_piece = board.board[new_position.row][new_position.column]
        if new_position_piece is not None and new_position_piece.color == self.color:
            print(f"Move invalid: target position {new_position} occupied by same color piece.")
            return False

        delta_x = new_position.row - self.position.row
        delta_y = new_position.column - self.position.column
        
        if abs(delta_x) == abs(delta_y) and abs(delta_x) > 0:
            step_x = delta_x // abs(delta_x)
            step_y = delta_y // abs(delta_y)
            for i in range(1, abs(delta_x)):
                row = self.position.row + step_x * i
                column = self.position.column + step_y * i
                if board.board[row][column] is not None:
                    print(f"Move invalid: path blocked at {Position(row, column)}")
                    return False
            return True
        
        if delta_x == 0 and abs(delta_y) > 0:
            step_y = delta_y // abs(delta_y)
            for i in range(1, abs(delta_y)):
                column = self.position.column + step_y * i
                if board.board[self.position.row][column] is not None:
                    print(f"Move invalid: path blocked at {Position(self.position.row, column)}")
                    return False
            return True
            
        if delta_y == 0 and abs(delta_x) > 0:
            step_x = delta_x // abs(delta_x)
            for i in range(1, abs(delta_x)):
                row = self.position.row + step_x * i
                if board.board[row][self.position.column] is not None:
                    print(f"Move invalid: path blocked at {Position(row, self.position.column)}")
                    return False
            return True
    
        print(f"Move invalid: move not recognized. deltaX: {delta_x}, deltaY: {delta_y}")
        return False
              
    def possible_moves(self, board=None):
        possible_moves = []
        for i in range(8):
            for j in range(8):
                new_position = Position(i, j)
                if new_position != self.position:
                    if self.is_valid_move(new_position, board):
                        possible_moves.append(new_position)
                        
        return possible_moves
