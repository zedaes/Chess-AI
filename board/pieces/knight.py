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