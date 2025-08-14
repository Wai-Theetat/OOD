class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
    
	def __str__(self):
		return str(self.data)

class BST:
	def __init__(self):
		self.root = None

	def insert(self, data):
		self.root = self.insert_think(self.root, data)		
  
	def insert_think(self, cur, data):
		if cur is None : return Node(data)
		else:
			if data < cur.data: cur.left = self.insert_think(cur.left, data)
			else : 				cur.right = self.insert_think(cur.right, data)
		return cur 

	def printTree(self, node, level = 0):
		if node != None:
			self.printTree(node.right, level + 1)
			print('     ' * level, node)
			self.printTree(node.left, level + 1)

class Solution:
	def main(self):
		inp = [int(i) for i in input('Enter Input : ').split()]

		tree = BST()
		for i in inp: tree.insert(i)
		tree.printTree(tree.root)	
  
s = Solution()
s.main()