class AVLNode:
	def __init__(self, data, left=None, right=None):
		self.__data = data
		self.__left = None if left is None else left
		self.__right = None if right is None else right
		self.__height = self.set_height()

	def get_data(self): return self.__data
	def set_data(self, new_data): self.__data = new_data

	def get_left(self) -> 'AVLNode': return self.__left
	def set_left(self, new_node): self.__left = new_node

	def get_right(self) -> 'AVLNode': return self.__right
	def set_right(self, new_node): self.__right = new_node

	def get_height_value(self):
		return self.__height

	def get_height(self, node: 'AVLNode'):
		return -1 if node is None else node.get_height_value()

	def set_height(self):
		lh = self.get_height(self.__left)
		rh = self.get_height(self.__right)
		self.__height = 1 + max(lh, rh)
		return self.__height

	def get_balance_val(self):
		return self.get_height(self.__left) - self.get_height(self.__right)

	def left_rotate(self, x: 'AVLNode') -> 'AVLNode':
		y = x.get_right()
		T2 = y.get_left() if y else None

		x.set_right(T2)
		if y:
			y.set_left(x)

		x.set_height()
		if y:
			y.set_height()
		return y if y is not None else x

	def right_rotate(self, x: 'AVLNode') -> 'AVLNode':
		y = x.get_left()
		T2 = y.get_right() if y else None

		x.set_left(T2)
		if y:
			y.set_right(x)

		x.set_height()
		if y:
			y.set_height()
		return y if y is not None else x

	def rebalance(self, node: 'AVLNode') -> 'AVLNode':
		if node is None:
			return node

		balance = node.get_balance_val()

		# Left heavy
		if balance > 1:
			if node.get_left().get_balance_val() < 0:
				node.set_left(self.left_rotate(node.get_left()))
			return self.right_rotate(node)

		# Right heavy
		if balance < -1:
			if node.get_right().get_balance_val() > 0:
				node.set_right(self.right_rotate(node.get_right()))
			return self.left_rotate(node)

		return node

	def __str__(self):
		return str(self.__data)


class AVLTree:
	def __init__(self, node: AVLNode = None):
		self.__root = None if node is None else node

	def get_root(self): return self.__root
	def set_root(self, node): self.__root = node

	def add(self, data):
		self.__root = self._add(self.__root, data)

	def _add(self, root_node: AVLNode, data):
		if root_node is None:
			return AVLNode(data)

		if data < root_node.get_data():
			root_node.set_left(self._add(root_node.get_left(), data))
		else:
			root_node.set_right(self._add(root_node.get_right(), data))

		root_node.set_height()
		return root_node.rebalance(root_node)

	def print_tree(self, node : AVLNode, level = 0):
		if node is not None:
			self.print_tree(node.get_right(), level + 1)
			print('     ' * level + ' ' +str(node.get_data()))
			self.print_tree(node.get_left(), level + 1)


class Solution:

	def find_maximum_sum_path(self, root: AVLNode):
		if root is None:
			return (0, [])

		left_sum, left_path = self.find_maximum_sum_path(root.get_left())
		right_sum, right_path = self.find_maximum_sum_path(root.get_right())

		if left_sum > right_sum:
			return (left_sum + root.get_data(), [root.get_data()] + left_path)
		else:
			return (right_sum + root.get_data(), [root.get_data()] + right_path)

	def main(self):
		apples = list(map(int, input("Enter tree nodes: ").split()))

		tree = AVLTree()
		for a in apples:
			tree.add(a)

		tree.print_tree(tree.get_root())
		print()

		max_sum, path = self.find_maximum_sum_path(tree.get_root())
		print("Path with maximum sum: " + " + ".join(map(str, path)) + f" = {max_sum}")


sol = Solution()
sol.main()
