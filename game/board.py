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
    def white_pieces(self):
        white_pawns = [pawn for pawn in self.pawns if pawn.color == 1]
        white_rooks = [rook for rook in self.rooks if rook.color == 1]
        white_knights = [knight for knight in self.knights if knight.color == 1]
        white_bishops = [bishop for bishop in self.bishops if bishop.color == 1]
        white_queens = [queen for queen in self.queens if queen.color == 1]
        white_kings = [king for king in self.kings if king.color == 1]
        
        return white_pawns + white_rooks + white_knights + white_bishops + white_queens + white_kings
    
    @property
    def black_pieces(self):
        black_pawns = [pawn for pawn in self.pawns if pawn.color == 0]
        black_rooks = [rook for rook in self.rooks if rook.color == 0]
        black_knights = [knight for knight in self.knights if knight.color == 0]
        black_bishops = [bishop for bishop in self.bishops if bishop.color == 0]
        black_queens = [queen for queen in self.queens if queen.color == 0]
        black_kings = [king for king in self.kings if king.color == 0]
        
        return black_pawns + black_rooks + black_knights + black_bishops + black_queens + black_kings
    
    @property
    def pieces(self):
        return self.white_pieces + self.black_pieces
    
    @property
    def board(self):
        board = [[None for _ in range(8)] for _ in range(8)]
        for piece in self.pieces:
            board[piece.position.row][piece.position.column] = piece
        
        return board
    
    def move_piece(self, piece, new_position):
        if not isinstance(piece, Piece):
            raise ValueError("The object to move must be an instance of Piece")
        
        if not isinstance(new_position, Position):
            raise ValueError("The new position must be an instance of Position")
        
        if self.is_within_bounds(new_position) and piece.is_valid_move(new_position, self):
            piece.has_moved = True
            current_position = piece.position
            self.board[current_position.row][current_position.column] = None
            target_piece = self.board[new_position.row][new_position.column]
            if target_piece is not None and target_piece in self.pieces:
                if type(target_piece) is Pawn:
                    self.pawns.remove(target_piece)
                elif type(target_piece) is Knight:
                    self.knights.remove(target_piece)
                elif type(target_piece) is Queen:
                    self.queens.remove(target_piece)
                elif type(target_piece) is King:
                    self.kings.remove(target_piece)
                elif type(target_piece) is Bishop:
                    self.bishops.remove(target_piece)
                elif type(target_piece) is Rook:
                    self.rooks.remove(target_piece)
                else:
                    raise ValueError("Invalid piece type")
                
            piece.position = Position(new_position.column, new_position.row)
        else:
            raise ValueError("Invalid move")
        
    def is_within_bounds(self, position):
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
        piece_symbols = {
            Pawn: "P",
            Rook: "R",
            Knight: "N",
            Bishop: "B",
            Queen: "Q",
            King: "K"
        }
        board_string = ""
        for row in self.board:
            row.reverse()
            for cell in row:
                if cell is None:
                    board_string += ". "
                else:
                    board_string += piece_symbols.get(type(cell), "X") + " "
                
            board_string += "\n"
            
        return board_string[::-1]

