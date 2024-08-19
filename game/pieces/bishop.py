from piece import Piece
from position import Position

class Bishop(Piece):
    def __init__(self, color=0, position=Position(0, 0)):
        super().__init__(color, position)
        self.x = self.position.row
        self.y = self.position.column
        
        if color == 0:
            self.image = 'img/whiteBishop.png'
        else:
            self.image = 'img/blackBishop.png'
            
    def isValidMove(self, newPosition=Position(0, 0), board=None):
        newPositionPiece = board.board[newPosition.row][newPosition.column]
        
        if newPositionPiece != None and newPositionPiece.color == self.color:
            return False
        
        deltaX = newPosition.row - self.position.row
        deltaY = newPosition.column - self.position.column
        
        if abs(deltaX) == abs(deltaY) and abs(deltaX) > 0:
            return True
        
        for i in range(1, abs(deltaX) - 1):
            x = self.position.row + (deltaX // abs(deltaX)) * i
            y = self.position.column + (deltaY // abs(deltaY)) * i
            if board.board[x][y] == None:
                return False
            
    
        
        
        
        
        
        
    
    def possibleMoves(self, board=None):
        pass