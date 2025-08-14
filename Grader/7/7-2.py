class Node:
	def __init__(self, data):
		self.__data = data
		self.__left = None
		self.__right = None
    
	@property
	def data(self): return self.__data
	@property
	def left(self): return self.__left
	@property
	def right(self): return self.__right
    
	@data.setter
	def data(self, new_data): self.__data = new_data
	@left.setter
	def left(self, new_node): self.__left = new_node
	@right.setter
	def right(self, new_node): self.__right = new_node


class BST:
	def __init__(self, root = None):
		self.__root = root

	@property
	def root(self) : return self.__root
 
	def insert(self, data):
		self.__root = self.__insert_think(self.__root, data)
		return 		
  
	def __insert_think(self, cur, data):
		if cur is None : return Node(data)
		else:
			if data < cur.data: cur.left = self.__insert_think(cur.left, data)
			else : 				cur.right = self.__insert_think(cur.right, data)
		return cur

	def print_tree(self, node, level = 0):
		if node != None:
			self.print_tree(node.right, level + 1)
			print('     ' * level, node.data)
			self.print_tree(node.left, level + 1)

	def print_inorder(self):
		self.__inorder_traverse_think(self.__root)	

	def __inorder_traverse_think(self, trav):
		if trav is not None:
			self.__inorder_traverse_think(trav.left)
			print(trav.data, end = ' ')
			self.__inorder_traverse_think(trav.right)
   
	def is_sum_exist(self, target):
		res = []
		self.__find_all_path_sum(self.__root, res)
		#print(res)
		return True if target in res else False
     
	def __find_all_path_sum(self, trav, res : list, sum = 0):
		if trav.left is None and trav.right is None:
			res.append(sum + self.__root.data)
		else:
			if trav.left  is not None: self.__find_all_path_sum(trav.left, res, sum + trav.left .data)
			if trav.right is not None: self.__find_all_path_sum(trav.right, res, sum + trav.right.data)

class Solution:
	def main(self):
		raw_inp, raw_target = input('Enter the values to insert into BST and target sum : ').split('/')
		
		inp = list(map(int, raw_inp.split()))
		target = int(raw_target)
		tree = BST()
  
		for i in inp: tree.insert(i)
		#tree.print_tree(tree.root)	
		
		print('Inorder Traversal of BST :',end = ' ')
		tree.print_inorder()
		
		target_status = tree.is_sum_exist(target)
		print(f'\nPath with sum {target} exists : {target_status}')
  
 
sol = Solution()
sol.main()