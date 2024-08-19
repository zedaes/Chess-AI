from piece import Piece
from position import Position

class King(Piece):
    def __init__(self, color=0, position=Position(0, 0)):
        super().__init__(color, position)
        self.row = self.position.row
        self.column = self.position.column
        
        if color == 0:
            self.image = 'img/whiteKing.png'
        else:
            self.image = 'img/blackKing.png'

    def isValidMove(self, newPosition=Position(0, 0), board=None):
        if not board:
            return False
        
        newPositionPiece = board.board[newPosition.row][newPosition.column]
        
        if newPositionPiece is not None and newPositionPiece.color == self.color:
            return False
        
        deltaX = abs(newPosition.row - self.position.row)
        deltaY = abs(newPosition.column - self.position.column)
        
        if deltaX <= 1 and deltaY <= 1:
            return not self.isInCheck(newPosition, board)
        
        if self.canCastle(newPosition, board):
            return True
        
        return False
    
    def isInCheck(self, position, board):
        for row in range(8):
            for col in range(8):
                piece = board.board[row][col]
                if piece is not None and piece.color != self.color:
                    if piece.isValidMove(position, board):
                        return True
        return False
    
    def canCastle(self, newPosition, board):
        if self.has_moved or self.isInCheck(self.position, board):
            return False
        
        if newPosition.column == 2 and newPosition.row == self.position.row:
            rook = board.board[self.position.row][0]
            if isinstance(rook, Piece) and not rook.has_moved:
                for col in range(1, 4):
                    if board.board[self.position.row][col] is not None or self.isInCheck(Position(self.position.row, col), board):
                        return False
                return True
        
        if newPosition.column == 6 and newPosition.row == self.position.row:
            rook = board.board[self.position.row][7]
            if isinstance(rook, Piece) and not rook.has_moved:
                for col in range(5, 7):
                    if board.board[self.position.row][col] is not None or self.isInCheck(Position(self.position.row, col), board):
                        return False
                return True
        
        return False
    
    def possibleMoves(self, board=None):
        possibleMoves = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                newPosition = Position(self.position.row + i, self.position.column + j)
                if 0 <= newPosition.row < 8 and 0 <= newPosition.column < 8:
                    if self.isValidMove(newPosition, board):
                        possibleMoves.append(newPosition)
        
        # Check for castling moves
        if self.canCastle(Position(self.position.row, 2), board):
            possibleMoves.append(Position(self.position.row, 2))
        if self.canCastle(Position(self.position.row, 6), board):
            possibleMoves.append(Position(self.position.row, 6))
        
        return possibleMoves