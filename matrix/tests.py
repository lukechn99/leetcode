import unittest
from .matrixapi import *
from .exceptions import *

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