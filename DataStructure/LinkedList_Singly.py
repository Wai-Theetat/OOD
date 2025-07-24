class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

class LinkedList:
	def __init__(self, new_list: list = None):
		self.__head = None
		self.__size = 0

		if new_list is not None:
			for item in new_list:
				self.append(item)

	@property
	def size(self):
		return self.__size

	@property
	def is_empty(self):
		return self.__size == 0

	def append(self, data):
		new_node = Node(data)
		if self.__head is None:
			self.__head = new_node
		else:
			current = self.__head
			while current.next is not None:
				current = current.next
			current.next = new_node
		self.__size += 1

	def remove(self, item):
		current = self.__head
		previous = None

		while current is not None:
			if current.value == item:
				if previous is None:
					self.__head = current.next  # Remove head
				else:
					previous.next = current.next
				self.__size -= 1
				return current.value
			previous = current
			current = current.next
		return None

	def remove_head(self):
		if self.__head is None:
			return None
		data = self.__head.value
		self.__head = self.__head.next
		self.__size -= 1
		return data

	def remove_tail(self):
		if self.__head is None:
			return None
		if self.__head.next is None:
			data = self.__head.value
			self.__head = None
			self.__size -= 1
			return data

		current = self.__head
		while current.next.next is not None:
			current = current.next
		data = current.next.value
		current.next = None
		self.__size -= 1
		return data

	def __str__(self):
		values = []
		current = self.__head
		while current is not None:
			values.append(str(current.value))
			current = current.next
		return " -> ".join(values) if values else "None"

	def print_list(self):
		print(self.__str__())


def main():
	test = LinkedList([1, 2, 3])
	test.append(4)
	print("List:", test)
	print("Size:", test.size)
	print("Is empty?", test.is_empty)

	test.remove(2)
	print("After removing 2:", test)

	test.remove_head()
	print("After removing head:", test)

	test.remove_tail()
	print("After removing tail:", test)

main()


#class Node:
#	def __init__(self, value):
#		self.value = value
#		self.next = None

#class LinkedList:
#	def __init__(self, new_list: list = None):
#		self.__head = None
#		self.__size = 0

#		if new_list is not None:
#			for item in new_list:
#				self.append(item)

#	@property
#	def size(self):
#		return self.__size

#	@property
#	def is_empty(self):
#		return self.__size == 0

#	def append(self, data):
#		new_node = Node(data)
#		if self.__head is None:
#			self.__head = new_node
#		else:
#			current = self.__head
#			while current.next is not None:
#				current = current.next
#			current.next = new_node
#		self.__size += 1

#	def remove(self, item):
#		current = self.__head
#		previous = None

#		while current is not None:
#			if current.value == item:
#				if previous is None:
#					self.__head = current.next  # Remove head
#				else:
#					previous.next = current.next
#				self.__size -= 1
#				return current.value
#			previous = current
#			current = current.next
#		return None

#	def remove_head(self):
#		if self.__head is None:
#			return None
#		data = self.__head.value
#		self.__head = self.__head.next
#		self.__size -= 1
#		return data

#	def remove_tail(self):
#		if self.__head is None:
#			return None
#		if self.__head.next is None:
#			data = self.__head.value
#			self.__head = None
#			self.__size -= 1
#			return data

#		current = self.__head
#		while current.next.next is not None:
#			current = current.next
#		data = current.next.value
#		current.next = None
#		self.__size -= 1
#		return data

#	def rt_list(self):
#		values = []
#		current = self.__head
#		while current is not None:
#			values.append(current.value)
#			current = current.next
#		return values

#	def print_list(self):
#		values = []
#		current = self.__head
#		while current is not None:
#			values.append(current.value)
#			current = current.next
#		print(values, end = '')