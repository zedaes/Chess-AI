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
        self.pawns = []
        self.rooks = []
        self.knights = []
        self.bishops = []
        self.queens = []
        self.kings = []
        
    @property
    def whitePieces(self):
        whitePawns = [pawn for pawn in self.pawns if pawn.color == 1]
        whiteRooks = [rook for rook in self.rooks if rook.color == 1]
        whiteKnights = [knight for knight in self.knights if knight.color == 1]
        whiteBishops = [bishop for bishop in self.bishops if bishop.color == 1]
        whiteQueens = [queen for queen in self.queens if queen.color == 1]
        whiteKings = [king for king in self.kings if king.color == 1]
        
        return whitePawns + whiteRooks + whiteKnights + whiteBishops + whiteQueens + whiteKings
    
    @property
    def blackPieces(self):
        blackPawns = [pawn for pawn in self.pawns if pawn.color == 0]
        blackRooks = [rook for rook in self.rooks if rook.color == 0]
        blackKnights = [knight for knight in self.knights if knight.color == 0]
        blackBishops = [bishop for bishop in self.bishops if bishop.color == 0]
        blackQueens = [queen for queen in self.queens if queen.color == 0]
        blackKings = [king for king in self.kings if king.color == 0]
        
        return blackPawns + blackRooks + blackKnights + blackBishops + blackQueens + blackKings
    
    @property
    def pieces(self):
        return self.whitePieces + self.blackPieces
    
    @property
    def board(self):
        board = [[None for _ in range(8)] for _ in range(8)]
        for piece in self.pieces:
            board[piece.position.row][piece.position.column] = piece
        
        return board
    
    def movePiece(self, piece, newPosition):
        if not isinstance(piece, Piece):
            raise ValueError("The object to move must be an instance of Piece")
        
        if not isinstance(newPosition, Position):
            raise ValueError("The new position must be an instance of Position")
        
        if self.isWithinBounds(newPosition) and piece.isValidMove(newPosition, self):
            currentPosition = piece.position
            self.board[currentPosition.row][currentPosition.column] = None
            dumbPiece = self.board[newPosition.row][newPosition.column]
            if dumbPiece is not None and dumbPiece in self.pieces:
                if type(dumbPiece) is Pawn:
                    self.pawns.remove(dumbPiece)
                elif type(dumbPiece) is Knight:
                    self.knights.remove(dumbPiece)
                elif type(dumbPiece) is Queen:
                    self.queens.remove(dumbPiece)
                elif type(dumbPiece) is King:
                    self.kings.remove(dumbPiece)
                elif type(dumbPiece) is Bishop:
                    self.bishops.remove(dumbPiece)
                elif type(dumbPiece) is Rook:
                    self.rooks.remove(dumbPiece)
                else:
                    raise ValueError("Invalid piece type")
                
            piece.position = Position(newPosition.column, newPosition.row)
        else:
            raise ValueError("Invalid move")
        
    def isWithinBounds(self, position):
        return 0 <= position.row < 8 and 0 <= position.column < 8
    
    def setup(self):
        self.pawns = [Pawn(0, Position(i, 1)) for i in range(8)] + [Pawn(1, Position(i, 6)) for i in range(8)]
        self.rooks = [Rook(0, Position(0, 0)), Rook(0, Position(7, 0)), Rook(1, Position(0, 7)), Rook(1, Position(7, 7))]
        self.knights = [Knight(0, Position(1, 0)), Knight(0, Position(6, 0)), Knight(1, Position(1, 7)), Knight(1, Position(6, 7))]
        self.bishops = [Bishop(0, Position(2, 0)), Bishop(0, Position(5, 0)), Bishop(1, Position(2, 7)), Bishop(1, Position(5, 7))]
        self.queens = [Queen(0, Position(3, 0)), Queen(1, Position(3, 7))]
        self.kings = [King(0, Position(4, 0)), King(1, Position(4, 7))]
            
    def display(self):
        pass
                   
    def __str__(self):
        pieceSymbols = {
            Pawn: "P",
            Rook: "R",
            Knight: "N",
            Bishop: "B",
            Queen: "Q",
            King: "K"
        }
        boardString = ""
        for row in self.board:
            row.reverse()
            for cell in row:
                if cell is None:
                    boardString += ". "
                else:
                    boardString += pieceSymbols.get(type(cell), "X") + " "
                
            boardString += "\n"
            
        return boardString[::-1]

board = Board()
board.setup()
print(board)
board.pawns.append(Pawn(1, Position(2, 2)))
print(board.pawns)
board.movePiece(board.knights[0], Position(2, 2))

print(board.pawns)