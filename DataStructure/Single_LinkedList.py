class Node:
	def __init__(self, value):
		self.value	= value
		self.next	= None
  
class LinkedList:
	def __init__(self, new_list : list = None):
		self.head = None
		self.size = 0

		if new_list != None:
			for item in new_list:
				self.append(item)

	def size(self):
		return self.size

	def is_empty(self):
		return self.size == 0

	def append_list(self, data): 
		new_node = Node(data)
	
		if self.head == None:
			self.head = new_node
		else:
			trav = self.head
			while trav.next != None:
				trav = trav.next
			trav.next = new_node
		self.size += 1

	def remove(self, item):
		if self.head == None : return

		trav = self.head
		prev = None
		while trav.next != None:
			if trav.value == item:
				self.size -= 1
				prev.next = trav.next
				return trav.value
			prev = trav
			trav = trav.next
		return None

	def remove_head(self):
		if self.head == None : return
		data = self.head.value
		self.head = self.head.next
		self.size -= 1
		return data
  
	def remove_tail(self):
		if self.head == None : return
		
		if self.head.next == None:
			self.head = None
			self.size -= 1
			return
		else:
			trav = self.head
			while trav.next.next != None:
				trav = trav.next
			trav.next = trav.next.next
			self.size -= 1
		
	def __str__(self):
		res = ''
		if self.head == None : res = res + 'None'
		else:
			trav = self.head
			while trav.next != None:
				res += f'{trav.value} '
				trav = trav.next
		return res

	def print_list(self):
		if self.head == None : print(self.head)
		else:
			trav = self.head
			while trav.next != None:
				print(f"{trav.value}", end=' ')
				trav = trav.next


def main():
	test = LinkedList()
	test.append_list(2)


	test.print_list()

main()