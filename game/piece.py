from position import Position

class Piece:
    def __init__(self, color = 0, position = Position(0, 0)):
        self.color = color
        self.position = position
        self.row = self.position.row
        self.column = self.position.column
    
    def is_valid_move(self, newPosition = Position(0, 0), board = None):
        raise NotImplementedError("This method should be overridden by subclasses.")
    
    def possible_moves(self, board = None):
        raise NotImplementedError("This method should be overridden by subclasses.")
    
    def get_color(self):
        if self.color == 0:
            return "white"
        else:
            return "black"
    
    def __str__(self):
        return f"{self.__class__.__name__}({self.color}, {self.position})"

