class Node:
	def __init__(self, data):
		self.__data = data
		self.__next = None
  
	@property
	def data(self):
		return self.__data

	@property
	def next(self):
		return self.__next

	@data.setter
	def data(self, new_data):
		self.__data = new_data

	@next.setter
	def next(self, new_node):
		self.__next = new_node

class LinkedList:
	def __init__(self, new_list: list = None):
			self.__head = None
			self.__size = 0

			if new_list is not None:
				for item in new_list:
					self.append(item)
	
	@property
	def head(self):
		return self.__head

	@head.setter
	def head(self, new_node):
		self.__head = new_node

	@property
	def size(self):
		return self.__size

	def is_empty(self):
		return self.__size == 0

	def append(self, new_data):
		new_node = Node(new_data)
	
		if self.__head is None:
			self.__head = new_node
		else:
			current = self.__head
			while current.next:
				current = current.next
			current.next = new_node
   
		self.__size += 1

	def remove(self, item):
		current = self.__head
		previous = None

		while current is not None:
			if current.data == item:
				if previous is None:
					self.__head = current.next  # Remove head
				else:
					previous.next = current.next
				self.__size -= 1
				return current.data
			previous = current
			current = current.next
		return None

	def remove_head(self):
		if self.__head is None:
			return None
		data = self.__head.data
		self.__head = self.__head.next
		self.__size -= 1
		return data

	def remove_tail(self):
		if self.__head is None:
			return None
		if self.__head.next is None:
			data = self.__head.data
			self.__head = None
			self.__size -= 1
			return data

		current = self.__head
		while current.next.next is not None:
			current = current.next
		data = current.next.data
		current.next = None
		self.__size -= 1
		return data

	def __str__(self):
		values = []
		current = self.__head
		while current is not None:
			values.append(str(current.data))
			current = current.next
		return " -> ".join(values) if values else "None"

	def print_list(self):
		print(self.__str__())
  
class ParentTracker:
	def __init__(self):
		self.__commits_ids  = LinkedList() #Linked list of ids data
		self.__parents_list = LinkedList() #Linked list of LinkedList of parent_ids
  
	def add(self, parent_id, child_id):
	
		ci : Node = self.__commits_ids.head
		pl = self.__parents_list.head
    
		#Find if child id is already store
		while ci:
			if ci.data == child_id:
				p = pl.data.head
				while p:
					if p.data == parent_id:
						return
					p = p.next
				#if no parrent just add it
				pl.data.append(parent_id)
				return
			ci = ci.next
			pl = pl.next
   
		#if not add child to list
		self.__commits_ids.append(child_id)
		new_parents = LinkedList()
		new_parents.append(parent_id)
		self.__parents_list.append(new_parents)

	def count_merges(self):
		cnt = 0
		traverse = self.__parents_list.head
		
		while traverse:
			#print(traverse.data)
			#if any children have more than 1 parrent
			if traverse.data.size > 1:
				cnt += 1
			traverse = traverse.next
		return cnt
 
def parse_branch(raw : str) -> LinkedList: 
	branch = LinkedList()
	parts = [x.strip() for x in raw.split("->")]

	#reverse commit set head to parrent
	for commit in reversed(parts):
		branch.append(commit)
	return branch

def is_same_repository(branches : list) -> bool:
	head : LinkedList = branches[0]
 
	for branch  in branches:
		if branch.head.data != head.head.data:
			return False
	return True

def main():
	raw_branches = input("Git History: ").strip().split('|')

	#variable declare
	branches 	= [] #[LinkedList(), LinkedList(), LinkedList(), ...]
	status		= False
	merge_cnt	= 0

	#convert input into Linked List
	branches = [parse_branch(raw_branch) for raw_branch in raw_branches]

	#check if all of these is same repo -> have same head
	status = is_same_repository(branches)
	if not status:
		print(f"Are these branches in the same repository? {status}")
		return

	#count merge
	track = ParentTracker()
	for branch in branches: 
		current = branch.head

		while current and current.next:
			track.add(current.data, current.next.data)
			current = current.next

	merge_cnt = track.count_merges()
	print(f"Are these branches in the same repository? {status}")
	print(f"{merge_cnt} Merge(s)")
 
main()