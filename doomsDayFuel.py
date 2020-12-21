# Doomsday Fuel
# =============

# Making fuel for the LAMBCHOP's reactor core is a tricky process because of the exotic matter
# involved. It starts as raw ore, then during processing, begins randomly changing between forms,
# eventually reaching a stable form. There may be multiple stable forms that a sample could
# ultimately reach, not all of which are useful as fuel. 

# Commander Lambda has tasked you to help the scientists increase fuel creation efficiency by
# predicting the end state of a given ore sample. You have carefully studied the different
# structures that the ore can take and which transitions it undergoes. It appears that, while
# random, the probability of each structure transforming is fixed. That is, each time the ore is
# in 1 state, it has the same probabilities of entering the next state (which might be the same
# state).  You have recorded the observed transitions in a matrix. The others in the lab have
# hypothesized more exotic forms that the ore can become, but you haven't seen all of them.

# Write a function solution(m) that takes an array of array of nonnegative ints representing how
# many times that state has gone to the next state and return an array of ints for each terminal
# state giving the exact probabilities of each terminal state, represented as the numerator for
# each state, then the denominator for all of them at the end and in simplest form. The matrix is
# at most 10 by 10. It is guaranteed that no matter which state the ore is in, there is a path
# from that state to a terminal state. That is, the processing will always eventually end in a
# stable state. The ore starts in state 0. The denominator will fit within a signed 32-bit integer
# during the calculation, as long as the fraction is simplified regularly. 

# For example, consider the matrix m:
# [
#   [0,1,0,0,0,1],  # s0, the initial state, goes to s1 and s5 with equal probability
#   [4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but with different probabilities
#   [0,0,0,0,0,0],  # s2 is terminal, and unreachable (never observed in practice)
#   [0,0,0,0,0,0],  # s3 is terminal
#   [0,0,0,0,0,0],  # s4 is terminal
#   [0,0,0,0,0,0],  # s5 is terminal
# ]
# So, we can consider different paths to terminal states, such as:
# s0 -> s1 -> s3
# s0 -> s1 -> s0 -> s1 -> s0 -> s1 -> s4
# s0 -> s1 -> s0 -> s5
# Tracing the probabilities of each, we find that
# s2 has probability 0
# s3 has probability 3/14
# s4 has probability 1/7
# s5 has probability 9/14
# So, putting that together, and making a common denominator, gives an answer in the form of
# [s2.numerator, s3.numerator, s4.numerator, s5.numerator, denominator] which is
# [0, 3, 2, 9, 14].

import unittest
import numpy as np
from fractions import Fraction

def isTerminal(row):
    for entry in row:
        if entry != 0:
            return False
    return True

# moves all terminal states to the top and switches probability indexes accordingly
def transform(m):
    # find the first terminal row
    nonterminals = []
    terminals = []
    for r in range(len(m)):
        if isTerminal(m[r]):
            terminals.append(r)
        else:
            nonterminals.append(r)
    scheme = terminals + nonterminals
    # switch rows following scheme
    matrix = []
    for r in range(len(scheme)):
        matrix.append(m[scheme[r]])
    m = matrix
    # switch columns following scheme
    for r in range(len(nonterminals) + 1, len(scheme)):
        row = []
        for c in range(len(scheme)):
            row.append(m[r][scheme[c]])
        m[r] = row
    return (m, len(terminals))

def findRMatrix(m, r):
    rmatrix = []
    for i in range(r, len(m)):
        row = m[i][:r]
        rowsum = float(sum(m[i]))
        row = [long(x) / rowsum for x in row]
        rmatrix.append(row)
    # print(rmatrix)
    return rmatrix

def findQMatrix(m, r):
    qmatrix = []
    for i in range(r, len(m)):
        row = m[i][r:]
        rowsum = float(sum(m[i]))
        row = [long(x) / rowsum for x in row]
        qmatrix.append(row)
    for row in qmatrix:
        print(row)
    return qmatrix

def commonDenom(prob):
    nums = []
    denoms = []
    for frac in prob:
        nums.append(frac.numerator)
        denoms.append(frac.denominator)
    lcm = np.lcm.reduce(np.array(denoms))
    for n in range(len(nums)):
        nums[n] = nums[n] * lcm / denoms[n]
    nums.append(lcm)
    return nums

# use absorbing Markov chains
def solution(m):
    if m == [[0]]:
        return [1, 1]
    info_m = transform(m)
    m = info_m[0]
    r = info_m[1]
    q = len(m) - r
    # use numpy ma
    rmatrix = np.squeeze(np.asarray(findRMatrix(m, r)))
    qmatrix = np.squeeze(np.asarray(findQMatrix(m, r)))
    identitymatrix = np.identity(q)
    # F = (I - Q)^-1
    fmatrix = np.linalg.inv(np.subtract(identitymatrix, qmatrix))
    # F*R
    fr = fmatrix.dot(rmatrix)
    # list of tuples
    probabilities = [Fraction(x).limit_denominator() for x in fr.tolist()[0]]
    return commonDenom(probabilities)

class Test(unittest.TestCase):
    def test_terminal_true(self):
        self.assertTrue(isTerminal([0, 0, 0, 0, 0]))
        self.assertTrue(isTerminal([0]))
    def test_terminal_false(self):
        self.assertFalse(isTerminal([0, 0, 0, 1, 0]))
        self.assertFalse(isTerminal([0, 2, 3, 1, 0, 0]))
    def test_transform(self):
        self.assertEqual(transform([[0, 2, 1, 0, 0],
                                    [0, 0, 0, 3, 4],
                                    [0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0]]),
                                    ([[0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0],
                                    [1, 0, 0, 0, 2],
                                    [0, 3, 4, 0, 0]], 3))
    def test1(self):
        print("\ntest 1")
        self.assertEqual(solution([[0, 2, 1, 0, 0],
                                   [0, 0, 0, 3, 4],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0]]), [7, 6, 8, 21])
    def test2(self):
        print("\ntest 2")
        self.assertEqual(solution([[0, 1, 0, 0, 0, 1],
                                   [4, 0, 0, 3, 2, 0],
                                   [0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0]]), [0, 3, 2, 9, 14])
    def test3(self):
        print("\ntest 3")
        self.assertEqual(solution([[1, 2, 3, 0, 0, 0],
                                   [4, 5, 6, 0, 0, 0],
                                   [7, 8, 9, 1, 0, 0],
                                   [0, 0, 0, 0, 1, 2],
                                   [0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0]]), [1, 2, 3])
    def test4(self):
        print("\ntest 4")
        self.assertEqual(solution([[0]]), [1, 1])
    def test5(self):
        print("\ntest 5")
        self.assertEqual(solution([[0, 0, 12, 0, 15, 0, 0, 0, 1, 8],
                                   [0, 0, 60, 0, 0, 7, 13, 0, 0, 0],
                                   [0, 15, 0, 8, 7, 0, 0, 1, 9, 0],
                                   [23, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                                   [37, 35, 0, 0, 0, 0, 3, 21, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]), [1, 2, 3, 4, 5, 15])
    def test6(self):
        print("\ntest 6")
        self.assertEqual(solution([[0, 7, 0, 17, 0, 1, 0, 5, 0, 2],
                                   [0, 0, 29, 0, 28, 0, 3, 0, 16, 0],
                                   [0, 3, 0, 0, 0, 1, 0, 0, 0, 0],
                                   [48, 0, 3, 0, 0, 0, 17, 0, 0, 0],
                                   [0, 6, 0, 0, 0, 1, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]), [4, 5, 5, 4, 2, 20])
    def test7(self):
        print("\ntest 7")
        self.assertEqual(solution([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]), [1, 1, 1, 1, 1, 5])
    def test8(self):
        print("\ntest 8")
        self.assertEqual(solution([[1, 1, 1, 0, 1, 0, 1, 0, 1, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [1, 0, 1, 1, 1, 0, 1, 0, 1, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [1, 0, 1, 0, 1, 0, 1, 1, 1, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]), [2, 1, 1, 1, 1, 6])
    def test9(self):
        print("\ntest 9")
        self.assertEqual(solution([[0, 86, 61, 189, 0, 18, 12, 33, 66, 39],
                                   [0, 0, 2, 0, 0, 1, 0, 0, 0, 0],
                                   [15, 187, 0, 0, 18, 23, 0, 0, 0, 0],
                                   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]), [6, 44, 4, 11, 22, 13, 100])
    def test10(self):
        print("\ntest 10")
        self.assertEqual(solution([[0, 0, 0, 0, 3, 5, 0, 0, 0, 2],
                                   [0, 0, 4, 0, 0, 0, 1, 0, 0, 0],
                                   [0, 0, 0, 4, 4, 0, 0, 0, 1, 1],
                                   [13, 0, 0, 0, 0, 0, 2, 0, 0, 0],
                                   [0, 1, 8, 7, 0, 0, 0, 1, 3, 0],
                                   [1, 7, 0, 0, 0, 0, 0, 2, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]), [1, 1, 1, 2, 5])

if __name__=="__main__": 
    # main()
    unittest.main()