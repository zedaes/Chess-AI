from piece import Piece
from position import Position

class Knight(Piece):
    def __init__(self, color=0, position=Position(0, 0)):
        super().__init__(color, position)
        self.x = self.position.row
        self.y = self.position.column
        
        if color == 0:
            self.image = 'img/whiteKnight.png'
        else:
            self.image = 'img/blackKnight.png'
            
    def isValidMove(self, newPosition=Position(0, 0), board=None):
        newPositionPiece = board.board[newPosition.row][newPosition.column]
        
        if newPositionPiece is not None and newPositionPiece.color == self.color:
            return False
        
        deltaX = newPosition.row - self.position.row
        deltaY = newPosition.column - self.position.column
        
        if (abs(deltaX) == 1 and abs(deltaY) == 2) or (abs(deltaX) == 2 and abs(deltaY) == 1):
            return True
        
        return False
              
    def possibleMoves(self, board=None):
        possibleMoves = []
        for i in range(0, 8):
            for j in range(0, 8):
                newPosition = Position(i, j)
                if newPosition != self.position:
                    if self.isValidMove(newPosition, board):
                        possibleMoves.append(newPosition)
                        
        return possibleMoves