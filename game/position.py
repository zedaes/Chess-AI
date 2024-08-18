class Position:
    def __init__(self, row, column):
        self.row = row
        self.column = column
    
    @classmethod
    def fromAlgebraic(cls, algebraicNotation):
        column = ord(algebraicNotation[0]) - ord('a')
        row = int(algebraicNotation[1]) - 1
        
        return cls(row, column)
    
    def toAlgebraic(self):
        column = chr(self.column + ord('a'))
        row = str(self.row + 1)

        return column + row
    
    def __eq__(self, other):
        return self.row == other.row and self.column == other.column
    
    def __str__(self):
        return self.toAlgebraic()
    
    def __repr__(self):
        return self.__str__()

    def isValid(self):
        return 0 <= self.row < 8 and 0 <= self.column < 8

