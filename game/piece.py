from position import Position

class Piece:
    def __init__(self, color = 0, position = Position(0, 0)):
        self.color = color
        self.position = position
        self.x = self.position.row
        self.y = self.position.column
    
    def move(self, newPosition = Position(0, 0)):
        if self.isValidMove(newPosition):
            self.position = newPosition
        else:
            raise ValueError("Invalid move for this piece.")
    
    def isValidMove(self, newPosition = Position(0, 0), board = None):
        raise NotImplementedError("This method should be overridden by subclasses.")
    
    def possibleMoves(self, board = None):
        raise NotImplementedError("This method should be overridden by subclasses.")
    
    def getColor(self):
        if self.color == 0:
            return "white"
        else:
            return "black"
    
    def __str__(self):
        return f"{self.__class__.__name__}({self.color}, {self.position})"

