from piece import Piece
from position import Position

class Pawn(Piece):
    def __init__(self, color=0, position=Position(0, 0)):
        super().__init__(color, position)
        self.row = self.position.row
        self.column = self.position.column
        
        if color == 0:
            self.image = 'img/whitePawn.png'
        else:
            self.image = 'img/blackPawn.png'
            
    def isValidMove(self, newPosition, board):
        direction = 1 if self.color == 0 else -1
        startRow = 1 if self.color == 0 else 6

        if newPosition.column == self.position.column:
            if newPosition.row == self.position.row + direction:
                return board.board[newPosition.row][newPosition.column] is None
            elif newPosition.row == self.position.row + 2 * direction and self.position.row == startRow:
                intermediateRow = self.position.row + direction
                
                return (board.board[newPosition.row][newPosition.column] is None and
                        board.board[intermediateRow][newPosition.column] is None)

        if abs(newPosition.column - self.position.column) == 1:
            if newPosition.row == self.position.row + direction:
                targetPiece = board.board[newPosition.row][newPosition.column]
                if targetPiece is not None and targetPiece.color != self.color:
                    return True
                if self.position.row == (3 if self.color == 0 else 4):
                    adjacentPawn = board.board[self.position.row][newPosition.column]
                    if isinstance(adjacentPawn, Pawn) and adjacentPawn.color != self.color and adjacentPawn.enPassant:
                        return True

        return False

    def promote(self, newPieceType):
        if (self.color == 0 and self.position.row == 7) or (self.color == 1 and self.position.row == 0):
            return newPieceType(self.color, self.position)
        return self