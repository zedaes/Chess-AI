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