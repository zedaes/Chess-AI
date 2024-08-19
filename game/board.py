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
                match type(dumbPiece):
                    case 'Pawn':
                        self.pawns.remove(dumbPiece)
                    case 'Rook':
                        self.rooks.remove(dumbPiece)
                    case 'Knight':
                        self.knights.remove(dumbPiece)
                    case 'Bishop':
                        self.bishops.remove(dumbPiece)
                    case 'King':
                        self.kings.remove(dumbPiece)
                    case 'Queen':
                        self.queens.remove(dumbPiece)
                    case _:
                        print("just give up...")
            piece.position = Position(newPosition.row, newPosition.column)
        else:
            raise ValueError("Invalid move")
        
    def isWithinBounds(self, position):
        return 0 <= position.row < 8 and 0 <= position.column < 8
    
    def setup(self):
        self.pawns = [Pawn(0, Position(1, i)) for i in range(8)] + [Pawn(1, Position(6, i)) for i in range(8)]
        self.rooks = [Rook(0, Position(0, 0)), Rook(0, Position(0, 7)), Rook(1, Position(7, 0)), Rook(1, Position(7, 7))]
        self.knights = [Knight(0, Position(0, 1)), Knight(0, Position(0, 6)), Knight(1, Position(7, 1)), Knight(1, Position(7, 6))]
        self.bishops = [Bishop(0, Position(0, 2)), Bishop(0, Position(0, 5)), Bishop(1, Position(7, 2)), Bishop(1, Position(7, 5))]
        self.queens = [Queen(0, Position(0, 3)), Queen(1, Position(7, 3))]
        self.kings = [King(0, Position(0, 4)), King(1, Position(7, 4))]
            
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
print(board.pawns)

board.pawns.remove(board.board[1][3])

board.movePiece(board.bishops[0], Position(3, 5))
print(board)

print(board.bishops[0].possibleMoves(board))