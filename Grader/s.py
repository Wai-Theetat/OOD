'''
 * กลุ่มที่  : 25010116
 * 67010441 ธีทัต ธรรมารุ่งเรือง
 * chapter : 7	item : 3	ครั้งที่ : 0003
 * Assigned : Thursday 14th of August 2025 10:58:23 AM --> Submission : Thursday 14th of August 2025 11:30:49 AM	
 * Elapsed time : 32 minutes.
 * filename : 7-3.py
'''
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
		self.__sum	= 0

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

	def get_sum(self, value):
		self.__sum = 0
		self.__think_sum(self.__root, value)
		return self.__sum

	def __think_sum(self, trav ,value):
		if trav is not None:
			if trav.data > value : trav.data *= value
			self.__sum += trav.data
			self.__think_sum(trav.left ,value)
			self.__think_sum(trav.right ,value)
   
class Solution:
	def main(self):
		print('**Sum of tree**')
		raw_inp, k = input('Enter input : ').split('/')
    
		inp  = list(map(int, raw_inp.split()))
		k	 = int(k)
	
		inp  = self.remove_dup(inp)
 
		tree = BST()
		for i in inp: tree.insert(i)
    
		print('\nTree before:')
		tree.print_tree(tree.root)
    
		sum1 = tree.get_sum(1)
		print(f'Sum of all nodes = {sum1}')
	
		print('\nTree after:')
		sum2 = tree.get_sum(k)
		tree.print_tree(tree.root)
		print(f'Sum of all nodes = {sum2}')
    
	def remove_dup(self, lst):
		lst2 = []
		for i in lst:
			if i not in lst2:
				lst2.append(i)
		return lst2
    
sol = Solution()
sol.main()