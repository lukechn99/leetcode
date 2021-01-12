import unittest
# from matrix.exceptions import *

##########################################################################
###################            Exceptions             ####################
class MatrixException(Exception):
    pass

class DimensionException(MatrixException):
    def __init__(self, message = "wrong dimensions for operation"):
        self.message = message
        super().__init__(self.message)
        
class InvalidException(MatrixException):
    def __init__(self, message = "not a valid matrix"):
        self.message = message
        super().__init__(self.message)
##########################################################################

class Matrix:
    def __init__(self, m = []):
        self.matrix = m
        
    def __str__(self):
        for row in self.matrix:
            print(row)
            
    def valid(self):
        if self.matrix == []:
            return True
        rowlen = len(self.matrix[0])
        for row in self.matrix:
            if len(row) != rowlen:
                return False
        return True
    
    def dim(self):
        if not self.valid():
            raise InvalidException
        if self.matrix == []:
            raise InvalidException
        return [len(self.matrix), len(self.matrix[0])]
    
    # m1 + m2
    def __add__(self, other):
        if not self.matrix.valid() or not other.valid():
            raise InvalidException
        dim1 = self.matrix.dim()
        dim2 = other.dim()
        if dim1 != dim2:
            raise DimensionException
        else:
            for i in range(len(dim1[0])):
                for j in range(len(dim1[1])):
                    self.matrix[i][j] = self.matrix[i][j] + other[i][j]
    
    def __sub__(self, other):
        if not self.matrix.valid() or not other.valid():
            raise InvalidException
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

##########################################################################
###################              Tests                ####################        

class Test(unittest.TestCase):
    # dim()
    def test1(self):
        m = Matrix([[1, 0],
                [0, 1]])
        self.assertEqual(m.dim(), [2, 2])
    def test2(self):
        m = Matrix()
        self.assertEqual(m.dim(), [0, 0])
    def test3(self):
        m = Matrix([[1, 2, 3],
                    [3, 4, 5],
                    [9, 0]])
        self.assertEqual(m.dim(), "not a valid matrix")

if __name__=="__main__":
    unittest.main()
    
##########################################################################