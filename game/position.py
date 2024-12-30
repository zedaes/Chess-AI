class Position:
    def __init__(self, column, row):
        self.row = row
        self.column = column
    
    @classmethod
    def from_algebraic(cls, algebraic_notation):
        column = ord(algebraic_notation[0]) - ord('a')
        row = int(algebraic_notation[1]) - 1
        
        return cls(row, column)
    
    def to_algebraic(self):
        column = chr(self.column + ord('a'))
        row = str(self.row + 1)

        return column + row
    
    def __eq__(self, other):
        return self.row == other.row and self.column == other.column
    
    def __str__(self):
        return self.to_algebraic()
    
    def __repr__(self):
        return self.__str__()

    def isValid(self):
        return 0 <= self.row < 8 and 0 <= self.column < 8

