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

	def get_size(self, node=None):
		if node is None:
			return 0
		return 1 + self.get_size(node.get_left()) + self.get_size(node.get_right())

	def left_rotate(self, root: 'AVLNode') -> 'AVLNode':
		pivot = root.get_right()
		left_subtree_of_pivot = pivot.get_left() if pivot else None

		root.set_right(left_subtree_of_pivot)
		if pivot:
			pivot.set_left(root)

		root.set_height()
		if pivot:
			pivot.set_height()

		return pivot if pivot else root

	def right_rotate(self, root: 'AVLNode') -> 'AVLNode':
		pivot = root.get_left()
		right_subtree_of_pivot = pivot.get_right() if pivot else None

		root.set_left(right_subtree_of_pivot)
		if pivot:
			pivot.set_right(root)

		root.set_height()
		if pivot:
			pivot.set_height()

		return pivot if pivot else root

	def rebalance(self, node: 'AVLNode') -> 'AVLNode':
		if node is None:
			return node

		balance = node.get_balance_val()

		# Left heavy
		if balance > 1:
			if node.get_left().get_balance_val() < 0:
				node.set_left(self.left_rotate(node.get_left()))  # LR case
			return self.right_rotate(node)  # LL case

		# Right heavy
		if balance < -1:
			if node.get_right().get_balance_val() > 0:
				node.set_right(self.right_rotate(node.get_right()))  # RL case
			return self.left_rotate(node)  # RR case

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


class Solution:
	def main(self):
		print('*** Simple but more ***')
        
		node_cnt, data, k = input('input  N node, Data, K small : ').split(',')

		node_cnt = int(node_cnt)
		data	 = list(map(int, data.split()))
		k_target = int(k)

		tree = AVLTree()

		for a in data:
			tree.add(a)
   
		k_res = self.find_k_smallest(tree.get_root(), k_target)
   
		print(k_res)
   
	def find_k_smallest(self, node : AVLNode, k_target):
		if node is None : return None
		left_size = node.get_size(node.get_left())
  
		if k_target == left_size + 1:
			return node.get_data()
		elif k_target <= left_size:
			return self.find_k_smallest(node.get_left(), k_target)
		else:
			return self.find_k_smallest(node.get_right(), k_target - left_size - 1)


sol = Solution()
sol.main()
