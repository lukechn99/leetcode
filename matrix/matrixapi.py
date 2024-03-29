import unittest
# from matrix.exceptions import *

###

##########################################################################
###################            Exceptions             ####################


class MatrixException(Exception):
    pass


class DimensionException(MatrixException):
    def __init__(self, message="wrong dimensions for operation"):
        self.message = message
        super().__init__(self.message)


class InvalidException(MatrixException):
    def __init__(self, message="not a valid matrix"):
        self.message = message
        super().__init__(self.message)
##########################################################################

##########################################################################
###################            Fractions              ####################


class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            self.num = self.num + other.num * self.den
        else:
            pass

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            self.num = self.num * other
        else:
            self.num = self.num * other.num
            self.den = self.den * other.den
        return self

##########################################################################


class Matrix:
    def __init__(self, m=[]):
        """Docstring"""

        self.matrix = m
        self.regular = self.regular()
        self.nonsingular = self.nonsingular()
        # refs are only recalculated if needed when the matrix changes
        self.ref = m
        self.ref_updated = False
        self.rref = m
        self.rref_updated = False
        self.rank = 0
        self.rank_updated =

    def regular(self):
        """Regular matrix

        A regular matrix is one that has only non-zero pivots when
        Gaussian eliminated with add and subtract elementary row
        operations in a descending fashion
        """
        # if already recorded and ref is found, just look in
        if not self.ref_updated:
            self.rowEchelon()
        for i in range(len(self.ref)):
            if self.ref[i][i] == 0:
                return False
        return True

    def nonsingular(self):
        """Nonsingular matrix

        A nonsingular matrix is one that has only non-zero pivots when
        Gaussian eliminated with add, subtract, and pivot row operations
        """

        return False

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
            return [0, 0]
        return [len(self.matrix), len(self.matrix[0])]

    def __str__(self):
        ret = "["
        for row in range(len(self.matrix) - 1):
            ret += "["
            for item in range(len(self.matrix[row]) - 1):
                ret += str(self.matrix[row][item]) + ", "
            ret += str(self.matrix[row][-1]) + "],\n"
        ret += "["
        for item in range(len(self.matrix[-1]) - 1):
            ret += str(self.matrix[-1][item]) + ", "
        ret += str(self.matrix[-1][-1]) + "]"
        ret += "]\n"
        return ret

    def __repr__(self):
        ret = "["
        for row in range(len(self.matrix) - 1):
            ret += "["
            for item in range(len(self.matrix[row]) - 1):
                ret += str(self.matrix[row][item]) + ", "
            ret += str(self.matrix[row][-1]) + "], "
        ret += "["
        for item in range(len(self.matrix[-1]) - 1):
            ret += str(self.matrix[-1][item]) + ", "
        ret += str(self.matrix[-1][-1]) + "]"
        ret += "]"
        return ret

    # m1 + m2
    def __add__(self, other):
        if not self.valid() or not other.valid():
            raise InvalidException
        dim1 = self.dim()
        dim2 = other.dim()
        if dim1 != dim2:
            raise DimensionException
        else:
            for i in range(dim1[0]):
                for j in range(dim1[1]):
                    self.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return self.matrix

    # m1 - m2
    def __sub__(self, other):
        if not self.valid() or not other.valid():
            raise InvalidException
        dim1 = self.dim()
        dim2 = other.dim()
        if dim1 != dim2:
            raise DimensionException
        else:
            for i in range(dim1[0]):
                for j in range(dim1[1]):
                    self.matrix[i][j] = self.matrix[i][j] - other[i][j]
        return self.matrix

    # can use scalars, or use as dot product
    # m1 * m2
    # m1 * n
    def __mul__(self, other):
        dim1 = self.dim()
        if isinstance(other, int) or isinstance(other, float):
            for i in range(dim1[0]):
                for j in range(dim1[1]):
                    self.matrix[i][j] = other * self.matrix[i][j]
        else:
            dim2 = other.dim()
            if dim1[1] != dim2[0]:
                raise DimensionException
            product = []
            for row in range(dim1[0]):
                p_row = []
                for col in range(dim2[1]):
                    other_col = [other_row[col] for other_row in other.matrix]
                    s = sum([x * y for x, y in zip(self.matrix[row], other_col)])
                    p_row.append(s)
                product.append(p_row)
            self.matrix = product
        return self.matrix

    # Row operations
    def swap_rows(self, n, m):
        temp = self.matrix[n]
        self.matrix[n] = self.matrix[m]
        self.matrix[m] = temp
        return self.matrix

    def add_rows(self, n, m):
        self.matrix[n] = [x + y for x, y in zip(n, m)]
        return self.matrix

    def sub_rows(self, n, m):
        self.matrix[n] = [x - y for x, y in zip(n, m)]
        return self.matrix

    def mul_rows(self, n, m):
        self.matrix[n] = [m * x for x in n]
        return self.matrix

    # Advanced matrix operations
    def transpose(self):
        """Method to transpose a matrix

        This method rebuilds a matrix into its transposed form
        """

        dim = self.dim()
        result = []
        for row in range(len(self.matrix)):
            for col in range(len(dim[0])):
                other_col = [other_row[col] for other_row in self.matrix]
                result.append(other_col)
        self.matrix = result
        return self.matrix

    # Gaussian elimination
    # sets the ref and ref_updated fields of Matrix
    # not tested yet
    # start
    #     for i = 1 to n
    #         set r(i) = i
    #     next i
    #     for j = 1 to n
    #         if mr(i),j = 0 for all i ≥ j, stop; print “A is singular”
    #         choose i>j such that mr(i),j is maximal
    #         interchange r(i) ←→ r(j)
    #         for i = j + 1 to n
    #             set lr(i)j = mr(i)j/mr(j)j
    #             for k = j + 1 to n + 1
    #                 set mr(i)k = mr(i)k − lr(i)jmr(j)k
    #             next k
    #         next i
    #     next j
    # end

    def rowEchelon(self):
        for row in self.matrix:
            # take the first row first item and use Fractions to eliminate
            # the first item of every succeeding row, then second row
            # second item and so on. If we reach a 0 when the corresponding
            # value in succeeding rows are not zero then this matrix is not
            # regular, if the matrix is reduced to ref with non-zero pivots
            # then the matrix is regular

            # perhaps we could store the ref version of a matrix in the
            # Matrix class.
            continue
        # if self.regular:
        #     # use the pivots to eliminate their column
        #     ref_matrix = self.matrix
        #     for i in range(len(self.matrix)):
        #         # use the ith row to create a fraction list to multiply
        #         scale = []
        #         for j in range(len(self.matrix)):
        #             scale.append(
        #                 Fraction(self.matrix[i][j], self.matrix[i][i]))
        #         sub_matrix = []
        #         for s in range(len(scale)):
        #             if s == 0:
        #                 sub_matrix.append([0 * x for x in self.matrix[s]])
        #             else:
        #                 sub_matrix.append([s * x for x in self.matrix[s]])
        #         ref_matrix = ref_matrix - sub_matrix
        #     self.ref_updated = True
        #     self.ref = ref_matrix

    # Gauss Jordan elimination
    def reducedRowEchelon(self):
        pass

    # **
    def __pow__(self, exponent):
        if self.matrix.dim()[0] != self.matrix.dim()[1]:
            raise DimensionException

##########################################################################
###################              Tests                ####################

# https://hackernoon.com/timing-tests-in-python-for-fun-and-profit-1663144571


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
        with self.assertRaises(InvalidException):
            m.dim()
    # swap(n, m)

    def test_swap(self):
        m1 = Matrix([[1, 2, 3],
                     [3, 4, 5],
                     [9, 0, 9]])
        m2 = Matrix([[3, 4, 5],
                     [1, 2, 3],
                     [9, 0, 9]])
        self.assertEqual(repr(m1.swap_rows(0, 1)), repr(m2))
    # add(m2)

    def test_add(self):
        m1 = Matrix([[1, 2, 3],
                     [4, 5, 6]])
        m2 = Matrix([[0, 0, 0],
                     [0, 0, 0]])
        result = Matrix([[1, 2, 3],
                         [4, 5, 6]])
        self.assertEqual(repr(m1 + m2), repr(result))

    def test_add_2(self):
        m1 = Matrix([[1, 2, 3],
                     [3, 4, 5],
                     [9, 0, 9]])
        m2 = Matrix([[1, 2, 3],
                     [4, 5, 6]])
        with self.assertRaises(DimensionException):
            m1 + m2

    def test_add(self):
        m1 = Matrix([[1, 2, 3],
                     [4, 5, 6],
                     [1, 1, 2]])
        m2 = Matrix([[1, 0, 0],
                     [0, 1, 0],
                     [0, 0, 1]])
        result = Matrix([[2, 2, 3],
                         [4, 6, 6],
                         [1, 1, 3]])
        self.assertEqual(repr(m1 + m2), repr(result))
    # sub(m2)

    def test_sub(self):
        m1 = Matrix([[1, 2, 3],
                     [4, 5, 6],
                     [1, 1, 2]])
        m2 = Matrix([[1, 0, 0],
                     [0, 1, 0],
                     [0, 0, 1]])
    # mul(n)

    def test_mul_constant(self):
        m1 = Matrix([[1, 2, 3],
                     [3, 4, 5],
                     [9, 0, 9]])
        self.assertEqual(repr(m1 * 5), repr(Matrix([[5, 10, 15],
                                                    [15, 20, 25],
                                                    [45, 0, 45]])))

    def test_mul_constant2(self):
        m1 = Matrix([[1, 2, 3],
                     [4, 5, 6]])
        self.assertEqual(repr(m1 * 0.5), repr(Matrix([[0.5, 1.0, 1.5],
                                                      [2.0, 2.5, 3.0]])))
    # mul(m2)

    def test_mul(self):
        m1 = Matrix([[1, 2, 3],
                     [3, 4, 5],
                     [9, 0, 9]])
        m2 = Matrix([[1, 4, 5, 9, 0],
                     [1, 1, 1, 0, 2],
                     [0, 0, 1, 2, 3]])
        result = Matrix([[3, 6, 10, 15, 13],
                         [7, 16, 24, 37, 23],
                         [9, 36, 54, 99, 27]])
        self.assertEqual(repr(m1 * m2), repr(result))

    def test_mul2(self):
        m1 = Matrix([[1, 2],
                     [1, 2],
                     [0, 5]])
        m2 = Matrix([[4, 1, 0, 0, 1],
                     [2, 1, 0, 1, 1]])
        result = Matrix([[8, 3, 0, 2, 3],
                         [8, 3, 0, 2, 3],
                         [10, 5, 0, 5, 5]])


if __name__ == "__main__":
    unittest.main()

##########################################################################
