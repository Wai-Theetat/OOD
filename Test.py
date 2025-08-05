class Node:
	def __init__(self, data = None):
		self.__data = data
		self.__next = None
  
	@property
	def next(self) : return self.__next
 
	@property
	def data(self) : return self.__data
 
	@next.setter
	def next(self, new_node) : self.__next = new_node
 
	@data.setter
	def data(self, new_data) : self.__data  = new_data 


class Queue:
	def __init__(self):
		self.__head = None
		self.__tail	= None
		self.__size = 0
  
	def enqueue(self, new_data):
		new_node = Node(new_data)
		if self.__tail:
			self.__tail.next = new_node
		else:
			self.__head = new_node
		self.__tail = new_node
		self.__size += 1
  
	def dequeue(self):
		if self.__head is None:
			raise IndexError("Dequeue from empty queue")
		removed_data = self.__head.data
		self.__head = self.__head.next
		if self.__head is None:
			self.__tail = None  # Queue is now empty
		self.__size -= 1
		return removed_data

	def	peek(self):
		if self.__head == None:
			raise IndexError("Peek from empty queue")
		return self.__head.data

	def is_empty(self):
		return self.__size == 0
 
	def get_size(self): return self.__size