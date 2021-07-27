'''
1. find the number
2. see if there is a right branch
	a. if there is, traverse the left branch of the right branch
	b. if there isn't, return right child
3. if there is no right branch, return parent

* cache the parent

class tree:
	self.left
	self.right
	self.val
'''

def findNext(tree, query):
	if not tree:
		return None

	def findNextHelper(tree, query, parent):
		if tree.val != query:
			if query > tree.val:
				return findNextHelper(tree.right, query, tree.val)
			else:
				return findNextHelper(tree.left, query, tree.val)
		else:
			if tree.right != None:
				ptr = tree.right
				while ptr.left != None:
					ptr = ptr.left
				return ptr.val
			else:
				return parent

	findNextHelper(tree, query, None)
