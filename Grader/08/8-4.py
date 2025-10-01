class BST:
	class Node:
		def __init__(self, data):
			self.data = data
			self.left = None
			self.right = None
			self.h = 1

		def update_height(self):
      
			if self.left:
				self.left.update_height()
			if self.right:
				self.right.update_height()
      
			left_h = self.left.h if self.left else 0
			right_h = self.right.h if self.right else 0
			self.h = 1 + max(left_h, right_h)
	
		def balance_factor(self):
			left_h = self.left.h if self.left else 0
			right_h = self.right.h if self.right else 0
   
			#print(f'Data : {self.data}, Height = {self.h},LH = {left_h}, RH  = {right_h}, BL = {left_h - right_h}')
   
			return left_h - right_h

	def __init__(self):
		self.root = None
	
	def insert(self, key):
		if not self.root:
			self.root = BST.Node(key)
		else:
			BST._insert(self.root, key)

	def _insert(node, key):
		if key < node.data:
			if node.left:
				BST._insert(node.left, key)
			else:
				node.left = BST.Node(key)
		else:
			if node.right:
				BST._insert(node.right, key)
			else:
				node.right = BST.Node(key)

	def _get_format(root, ans = ""):
		if root:
			temp = ""
			if root.right:
				temp += BST._get_format(root.right, ans + "     ")
			temp += f"{ans}{root.data}\n"
			if root.left:
				temp += BST._get_format(root.left, ans + "     ")
			return temp
		return ""
	
	def __str__(self):
		return BST._get_format(self.root)

class Solution:
	
	def main(self):
		tree = BST()
    
		print("**********IsAVL**********")
		for i in list(map(int, input("Enter numbers to insert in the tree: ").split())):
			tree.insert(i)

		print("Tree:")
		print(tree)

		print("Is AVL???:", self.is_AVL(tree.root))
  
	def is_AVL(self, node: BST.Node):
		if node is None:
			return True

		node.update_height()

		if abs(node.balance_factor()) > 1:
			return False

		return self.is_AVL(node.left) and self.is_AVL(node.right)

sol = Solution()
sol.main()