class Node:
	def __init__(self, value):
		self.__value = value
		self.__prev = None
		self.__next = None

	@property
	def value(self):
		return self.__value

	@value.setter
	def value(self, new_value):
		self.__value = new_value

	@property
	def next(self):
		return self.__next

	@next.setter
	def next(self, node):
		self.__next = node

	@property
	def prev(self):
		return self.__prev

	@prev.setter
	def prev(self, node):
		self.__prev = node

class LinkedList:
	def __init__(self):
		self.__head = None
		self.__tail = None
		self.__size = 0

	@property
	def size(self):
		return self.__size

	def is_empty(self):
		return self.__head is None

	def add_new_head(self, value):
		new_node = Node(value)
		new_node.next = self.__head

		if not self.is_empty():
			self.__head.prev = new_node
		else:
			self.__tail = new_node

		self.__head = new_node
		self.__size += 1
		return new_node

	def append(self, value):
		new_node = Node(value)

		if self.is_empty():
			self.__head = self.__tail = new_node
		else:
			self.__tail.next = new_node
			new_node.prev = self.__tail
			self.__tail = new_node

		self.__size += 1
		return new_node

	def insert(self, value, index):
		if index < 0 or index > self.__size:
			raise IndexError("Index out of bounds")
		if index == 0:
			return self.prepend(value)
		if index == self.__size:
			return self.append(value)

		new_node = Node(value)
		mid = self.__size // 2

		if index <= mid:
			current = self.__head
			for _ in range(index - 1):
				current = current.next
		else:
			current = self.__tail
			for _ in range(self.__size - index):
				current = current.prev

		new_node.next = current.next
		new_node.prev = current
		if current.next:
			current.next.prev = new_node
		current.next = new_node

		self.__size += 1
		return new_node

	def delete(self, index):
		if self.is_empty():
			raise IndexError("Remove from empty list")
		if index < 0 or index >= self.__size:
			raise IndexError("Index out of bounds")

		if index == 0:
			return self.delete_head()
		if index == self.__size - 1:
			return self.delete_tail()

		mid = self.__size // 2
		if index <= mid:
			current = self.__head
			for _ in range(index):
				current = current.next
		else:
			current = self.__tail
			for _ in range(self.__size - index - 1):
				current = current.prev

		current.prev.next = current.next
		current.next.prev = current.prev
		self.__size -= 1
		return current.value

	def delete_head(self):
		if self.is_empty():
			raise IndexError("Remove from empty list")

		removed_value = self.__head.value
		if self.__head == self.__tail:
			self.__head = self.__tail = None
		else:
			self.__head = self.__head.next
			self.__head.prev = None

		self.__size -= 1
		return removed_value

	def delete_tail(self): 
		if self.is_empty():
			raise IndexError("Remove from empty list")

		removed_value = self.__tail.value
		if self.__head == self.__tail:
			self.__head = self.__tail = None
		else:
			self.__tail = self.__tail.prev
			self.__tail.next = None

		self.__size -= 1
		return removed_value

	def index_of(self, value):
		current = self.__head
		index = 0
		while current:
			if current.value == value:
				return index
			current = current.next
			index += 1
		return -1

	def __str__(self):
		values = []
		current = self.__head
		while current:
			values.append(str(current.value))
			current = current.next
		return " <-> ".join(values) + " -> None" if values else "Empty list"

	def __getitem__(self, index):
		if index < 0:
			index += self.__size
		if index < 0 or index >= self.__size:
			raise IndexError("Index out of bounds")

		mid = self.__size // 2
		if index <= mid:
			current = self.__head
			for _ in range(index):
				current = current.next
		else:
			current = self.__tail
			for _ in range(self.__size - index - 1):
				current = current.prev

		return current.value

	def __setitem__(self, index, value):
		if index < 0:
			index += self.__size
		if index < 0 or index >= self.__size:
			raise IndexError("Index out of bounds")

		mid = self.__size // 2
		if index <= mid:
			current = self.__head
			for _ in range(index):
				current = current.next
		else:
			current = self.__tail
			for _ in range(self.__size - index - 1):
				current = current.prev

		current.value = value
  
	#clear all item of linked-list
	def clear(self):
		self.__head = self.__tail = None
		self.__size = 0

class Ant:
	def __init__(self, name):
		self.__name = name

	def __str__(self): 
		return self.__name

class WorkerAnt(Ant):
	def __init__(self, name):
		super().__init__(name)
		self.__carry  = 2
		self.__damage = 5
  
	@property
	def carry(self): return self.__carry
	@property
	def damage(self): return self.__damage

class ArmyAnt(Ant):
	def __init__(self, name):
		super().__init__(name)
		self.__carry  = 5
		self.__damage = 10

	@property
	def carry(self): return self.__carry
	@property
	def damage(self): return self.__damage

#เหล่ามดจะถูกจัดเก็บอยู่ใน linked list เดียวกัน
class Population(LinkedList):
	def __init__(self, worker, army):
		super().__init__()
  
		self.__latest_W_id = 0
		self.__latest_A_id = 0
  
		self.add_ant(worker, 'W')
		self.add_ant(army, 'A')

	
	def add_ant(self, value, ant_type):
		pass


	@property
	def latest_W(self): return self.__latest_W_id
	@property
	def latest_A(self): return self.__latest_A_id

	@latest_W.setter
	def latest_W(self, val): self.__latest_W_id = val
	@latest_A.setter
	def latest_A(self, val): self.__latest_A_id = val
 
 
#หากราชินีโกรธครบ 3 ครั้ง รังมดจะแตกและหยุดทำงานทันที
class Colony:
	def __init__(self, wp, ap):
		self.__angry = 0
		self.__ant_population = Population(wp, ap)

def main():
	print("***This colony is our home***")
	raw_ant_population, raw_commands = input("Enter input : ").split('/')

	w_ant, a_ant = raw_ant_population.split() 

main()