from position import Position
from piece import Piece

from pieces.bishop import Bishop
from pieces.king import King
from pieces.knight import Knight
from pieces.pawn import Pawn
from pieces.queen import Queen
from pieces.rook import Rook

class Board:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
    
    def placePiece(self, piece, position):
        if self.isWithinBounds(position) and self.board[position.row][position.column] is None:
            self.board[position.row][position.column] = piece
            piece.position = position
        else:
            raise ValueError("Invalid position or position already occupied")
    
    def movePiece(self, piece, newPosition):
        if not isinstance(piece, Piece):
            raise ValueError("The object to move must be an instance of Piece")
        
        if not isinstance(newPosition, Position):
            raise ValueError("The new position must be an instance of Position")
        
        if self.isWithinBounds(newPosition) and piece.isValidMove(newPosition, self):
            currentPosition = piece.position
            self.board[currentPosition.row][currentPosition.column] = None
            self.board[newPosition.row][newPosition.column] = piece
            piece.move(newPosition)
        else:
            raise ValueError("Invalid move")
        
    def isWithinBounds(self, position):
        return 0 <= position.row < 8 and 0 <= position.column < 8
        
    def __str__(self):
        piece_symbols = {
            Pawn: "P",
            Rook: "R",
            Knight: "N",
            Bishop: "B",
            Queen: "Q",
            King: "K"
        }
        boardStr = ""
        for row in self.board:
            for cell in row:
                if cell is None:
                    boardStr += ". "
                else:
                    boardStr += piece_symbols.get(type(cell), "X") + " "
            boardStr += "\n"
        return boardStr
    
if __name__ == "__main__":
    board = Board()
    pawnWhite = Pawn(color=0, position=Position(1, 0))
    pawnBlack = Pawn(color=1, position=Position(6, 0))
    rookWhite = Rook(color=0, position=Position(0, 0))
    knightWhite = Knight(color=0, position=Position(0, 1))
    bishopWhite = Bishop(color=0, position=Position(0, 2))
    queenWhite = Queen(color=0, position=Position(0, 3))
    kingWhite = King(color=0, position=Position(0, 4))
    
    board.placePiece(pawnWhite, Position(1, 0))
    board.placePiece(pawnBlack, Position(6, 0))
    board.placePiece(rookWhite, Position(0, 0))
    board.placePiece(knightWhite, Position(0, 1))
    board.placePiece(bishopWhite, Position(0, 2))
    board.placePiece(queenWhite, Position(0, 3))
    board.placePiece(kingWhite, Position(0, 4))
    
    print("Initial Board:")
    print(board)
    
    board.movePiece(pawnWhite, Position(3, 0))  # White pawn moves two steps forward
    print("After White Pawn Move:")
    print(board)
    
    board.movePiece(pawnBlack, Position(5, 0))  # Black pawn moves one step forward
    print("After Black Pawn Move:")
    print(board)