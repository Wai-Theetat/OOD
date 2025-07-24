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
				self.__size += 1

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

	def get_head(self):
		return self.__head

	def set_head(self, data):
		self.__head = data

	def get_tail(self):
		traverse = self.__head
		while traverse.next != None:
			traverse = traverse.next
		return traverse		
  
	def swap(self, v1, v2):
		tmp = v1.value
		v1.value  = v2.value
		v2.value  = tmp
  
	def __str__(self):
		ans = []
		node = self.__head
		while node:
			ans.append(str(node.value))
			node = node.next
		return '->'.join(ans)

def do_buble_sort(nums : LinkedList):
	iterate = 0
	length  = nums.size
 
	while iterate < length:
		swap = False	
		tmp = nums.get_head()
		while tmp.next:
			#print(tmp.value, tmp.next.value)
			if tmp.value > tmp.next.value:
				print(f"\nSwapping {tmp.value } and {tmp.next.value}")
				swap = True
				nums.swap(tmp, tmp.next)
				print(f"List: {nums}")
			tmp = tmp.next
   
		if not swap:
			break
		iterate += 1

def main():
	print("*****Bubble Sort Linked List*****")
	nums = LinkedList(list(map(int,input("Enter Input: ").split(','))))

	print("Input List:",nums)
	print("_______________________________________")
	do_buble_sort(nums)
	print("_______________________________________")
	print(f"Sorted List: {nums}")
 
main()