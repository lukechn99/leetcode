# Given an n x n board with a single bishop and a single knight, the knight needs to get from
# point A to point B without crossing paths with the bishop, the knight must either avoid the
# bishop or capture the bishop. Find the length of the shortest path from A to B

import unittest

# takes a bishop row and column and generates the points the knight cannot go to
def dangerSquares(n, brow, bcol):
    board = [[1] * n] * n
    for i in range(n):
        for j in range(n):
            if i == brow and j == bcol:
                board[i][j] = 1
            elif abs(i - brow) == abs(j - bcol):
                board[i][j] = 0
    print(board)
    return board

def legal(n, x, y):
    if x >= 0 and x < n and y >= 0 and y < n:
        return True
    return False

def knightAdj(n, board, krow, kcol):
    adjmoves = []
    move_offsets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1), (1, -2), (1, 2), (2, -1), (2, 1)]
    for r, c in move_offsets:
        

dangerSquares(4, 0, 0)
dangerSquares(4, 1, 2)
# main method
def moves(n, startRow, startCol, endRow, endCol, bishopRow, bishopCol):
	# generate the squares the knight cannot go to
	# mark them in a binary matrix
	# depth first search? Dijkstra's?
	pass

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(dangerSquares(4, 0, 0), [[1, 1, 1, 1],
                                                  [1, 0, 1, 1],
                                                  [1, 1, 0, 1],
                                                  [1, 1, 1, 0]])
    def test2(self):
        self.assertEqual(dangerSquares(4, 1, 2), [[1, 0, 1, 0],
                                                  [1, 1, 1, 1],
                                                  [1, 0, 1, 0],
                                                  [0, 1, 1, 1]])

# if __name__=="__main__": 
#     # main()
#     unittest.main()