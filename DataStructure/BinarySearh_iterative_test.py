class Node:
	def __init__(self, value):
		self.__value = value
		self.__prev = None
		self.__next = None

	@property
	def value(self):
		return self.__value

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

	def is_empty(self):
		return self.__head is None

	def insert_start(self, value):
		new_node = Node(value)
		new_node.next = self.__head

		if not self.is_empty():
			self.__head.prev = new_node
		else:
			self.__tail = new_node
		self.__head = new_node
		self.__size += 1

	def insert_end(self, value):
		new_node = Node(value)

		if self.is_empty():
			self.__head = self.__tail = new_node
		else:
			self.__tail.next = new_node
			new_node.prev = self.__tail
			self.__tail = new_node
		self.__size += 1

	def insert_any(self, value, index):
		if index < 0 or index > self.__size:
			raise IndexError("Out of bounds")
		if index == 0:
			self.insert_start(value)
			return
		if index == self.__size:
			self.insert_end(value)
			return

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

	def remove(self, index):
		if self.is_empty():
			raise IndexError("Remove from empty list")
		if index < 0 or index >= self.__size:
			raise IndexError("Index out of bounds")

		if index == 0:
			return self.remove_head()
		if index == self.__size - 1:
			return self.remove_tail()

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

	def remove_head(self):
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

	def remove_tail(self):
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

	def print_head_to_tail(self):
		current = self.__head
		while current:
			print(current.value, end=", ")
			current = current.next
		print("None")

	def print_tail_to_head(self):
		current = self.__tail
		while current:
			print(current.value, end=", ")
			current = current.prev
		print("None")


def main():
	dll = LinkedList()
	dll.insert_start(10)
	dll.insert_end(20)
	dll.insert_end(30)
	dll.insert_start(5)

	print("Forward:")
	dll.print_head_to_tail()

	print("Backward:")
	dll.print_tail_to_head()

	print("\nInsert text at index 2:")
	dll.insert_any("This is Txet", 2)
	dll.print_head_to_tail()

	print("\nRemoved head:", dll.remove_head())
	dll.print_head_to_tail()

	print("\nRemoved tail:", dll.remove_tail())
	dll.print_head_to_tail()

	print("\nRemoved at index 1:", dll.remove(1))
	dll.print_head_to_tail()

main()
