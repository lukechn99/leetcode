import unittest

def isSymmetric(matrix):
	# error checking for valid matrix
	if matrix == None or matrix == [] or isinstance(matrix[0], int) or len(matrix) != len(matrix[0]):
		return False

	for i in range(len(matrix)):
		for j in range(i, len(matrix[0])):
			if matrix[i][j] != matrix[j][i]:
				return False
	return True

 #######################
###     UNITTESTS     ###
 #######################

class Test(unittest.TestCase):
	def test_symmetricalOdd(self):
		matrix = [[1,0,0],[0,1,0],[0,0,1]]
		self.assertTrue(isSymmetric(matrix))
	def test_symmetricalEven(self):
		matrix = [[2,2,0,0],[2,0,0,0],[0,0,0,2],[0,0,2,2]]
		self.assertTrue(isSymmetric(matrix))
	def test_empty(self):
		matrix = []
		self.assertFalse(isSymmetric(matrix))
	def test_none(self):
		self.assertFalse(isSymmetric(None))
	def test_list(self):
		matrix = [1,2,0,3]
		self.assertFalse(isSymmetric(matrix))
	def test_nonSymmetric(self):
		matrix = [[1,1,0],[1,2,1],[0,0,2]]
		self.assertFalse(isSymmetric(matrix))
if __name__ == '__main__':
	unittest.main()
