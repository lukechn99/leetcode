from .exceptions import *

class Matrix:
    def __init__(self, m = [[]]):
        self.matrix = m
        
    def __str__(self):
        for row in self.matrix:
            print(row)
            
    def dim(self):
        if self.matrix == []:
            raise InvalidException
        return [len(self.matrix), len(self.matrix[0])]
    
    # m1 + m2
    def __add__(self, other):
        dim1 = self.matrix.dim()
        dim2 = other.dim()
        if dim1 != dim2:
            raise DimensionException
        else:
            for i in range(len(dim1[0])):
                for j in range(len(dim1[1])):
                    self.matrix[i][j] = self.matrix[i][j] + other[i][j]
    
    def __sub__(self, other):
        dim1 = self.matrix.dim()
        dim2 = other.dim()
        if dim1 != dim2:
            raise DimensionException
        else:
            for i in range(len(dim1[0])):
                for j in range(len(dim1[1])):
                    self.matrix[i][j] = self.matrix[i][j] - other[i][j]
    
    def __mul__(self, other):
        dim1 = self.matrix.dim()
        if isinstance(other, int):
            for i in range(len(dim1[0])):
                for j in range(len(dim1[1])):
                    self.matrix[i][j] = other * self.matrix[i][j]
        else:
            dim2 = other.dim()
            if dim1[0] != dim2[1] or dim1[1] != dim2[0]:
                raise DimensionException

    def transpose(self):
        pass
    
    def rref(self):
        pass
    
    # **
    def __pow__(self, exponent):
        if self.matrix.dim()[0] != self.matrix.dim()[1]:
            raise DimensionException
        
        
    
    
    
        