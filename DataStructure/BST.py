class Node:
	def __init__(self, data = None):
		self.__data = data
		self.__left = None
		self.__right= None

	@property
	def data(self): return self.__data
 
	@property
	def left(self): return self.__left

	@property
	def right(self): return self.__right
 
	@data.setter
	def data(self, value):
		self.__data = value

	@left.setter
	def left(self, value):
		self.__left = value

	@right.setter
	def right(self, value):
		self.__right = value

class BST:	
	def __init__(self, node = None):
		self.__root = node

		



newTree = BST()