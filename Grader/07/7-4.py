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
   
	def find_treasure_and_escape(self, path, treasure, escape, trav, found_treasure=False):
		if trav is None:
			return False  # not found

		path.append(trav.data)

		if not found_treasure:
			# Tresure
			if trav.data == treasure:
				print(f'Found Treasure !!!')

				if trav.data == escape:
					print(f'Found Escape !!!')
					self.print_path(path, True)
					return True
				else:
					self.print_path(path, False)
		
				found_treasure = True  # switch mode
			else:
				self.print_path(path, False)
		else:
		# Already found treasure, now looking for escape
			if trav.data == escape:
				print(f'Found Escape !!!')
				self.print_path(path, True)
				return True
			else:
				self.print_path(path, False)


		if self.find_treasure_and_escape(path, treasure, escape, trav.left, found_treasure):
			return True
		if self.find_treasure_and_escape(path, treasure, escape, trav.right, found_treasure):
			return True

		path.pop()
		return False

  
	def print_path(self, path, type_bool):
		
		print('✅',end=' ') if type_bool is True else print('❌',end=' ')

		for i in range(0, len(path)):
			print(f'{path[i]}', end=' -> ' if i<len(path)-1 else '\n')	



class Solution:
	def main(self):
		raw_inp, tresure, escape = input('Enter Input : ').split('/')
    
		inp  = list(map(int, raw_inp.split()))
		tresure	 = (int(tresure), 'Tresure')
		escape	 = (int(escape), 'Escape')

		inp  = self.remove_dup(inp)
 
		tree = BST()
		for i in inp: tree.insert(i)
    
		tree.print_tree(tree.root)
		print('-------------------------------------------------')
		path = []
  
		if not tree.find_treasure_and_escape(path, tresure[0], escape[0], tree.root):
			print('>>> Mission Failed <<<')
		else:
			print('>>> Mission Complete <<<')

    #❌✅
    
    
	def remove_dup(self, lst):
		lst2 = []
		for i in lst:
			if i not in lst2:
				lst2.append(i)
		return lst2


sol = Solution()
sol.main()