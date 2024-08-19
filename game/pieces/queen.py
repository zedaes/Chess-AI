from piece import Piece
from position import Position

class Queen(Piece):
    def __init__(self, color=0, position=Position(0, 0)):
        super().__init__(color, position)
        self.x = self.position.row
        self.y = self.position.column
        
        if color == 0:
            self.image = 'img/whiteQueen.png'
        else:
            self.image = 'img/blackQueen.png'
            
    def isValidMove(self, newPosition=Position(0, 0), board=None):
        newPositionPiece = board.board[newPosition.row][newPosition.column]
        
        if newPositionPiece is not None and newPositionPiece.color == self.color:
            return False
        
        deltaX = newPosition.row - self.position.row
        deltaY = newPosition.column - self.position.column
        
        if abs(deltaX) == abs(deltaY) and abs(deltaX) > 0:
            stepX = deltaX // abs(deltaX)
            stepY = deltaY // abs(deltaY)
            
            for i in range(1, abs(deltaX)):
                x = self.position.row + stepX * i
                y = self.position.column + stepY * i
                if board.board[x][y] is not None:
                    return False
            return True
        
        if deltaX == 0 and abs(deltaY) > 0:
            stepY = deltaY // abs(deltaY)
            for i in range(1, abs(deltaY)):
                y = self.position.column + stepY * i
                if board.board[self.position.row][y] is not None:
                    return False
            return True
            
        if deltaY == 0 and abs(deltaX) > 0:
            stepX = deltaX // abs(deltaX)
            for i in range(1, abs(deltaX)):
                x = self.position.row + stepX * i
                if board.board[x][self.position.column] is not None:
                    return False
            return True
        
        return False
              
    def possibleMoves(self, board=None):
        possibleMoves = []
        for i in range(8):
            for j in range(8):
                newPosition = Position(i, j)
                if newPosition != self.position:
                    if self.isValidMove(newPosition, board):
                        possibleMoves.append(newPosition)
                        
        return possibleMoves
