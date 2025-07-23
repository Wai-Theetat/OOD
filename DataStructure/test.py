class Queue:
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return len(self.__items) == 0

    def enqueue(self, item):
        self.__items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.__items.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.__items[0]

    def size(self):
        return len(self.__items)

    def __str__(self):
        return str(self.__items)

    def contains(self, value):
        for item in self.__items:
            if item == value:
                return True
        return False

class Stack:
    def __init__(self):
        self.__items = []
 
    def push(self, item):
        self.__items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.__items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.__items[-1]

    def is_empty(self):
        return len(self.__items) == 0

    def size(self):
        return len(self.__items)

    def __str__(self):
        return str(self.__items)

    
def is_groupable(group: Queue, student: str) -> bool:
	
	if (student == "Green" and group.contains("Pink") and not group.contains("Blue")):
		return False
	
	if (student == "Pink" and group.contains("Green") and not group.contains("Blue")):
		return False

	if (student == "Blue" and group.contains("Yellow") and not group.contains("Red")):
		return False
	
	if (student == "Yellow" and group.contains("Blue") and not group.contains("Red")):
		return False

	return True

def main():
    
	maxmem, raw_students = input("***Make a group***\nEnter input : ").split(',')
	
	maxmem		= int(maxmem)
	rejected	= Queue()
	students	= Queue()
	groups		= Stack()

	for tmp in raw_students.split():
		students.enqueue(tmp)
	
	current_group = Queue()
 
	while not students.is_empty():
		student = students.dequeue()
		
		if current_group.size() >= maxmem:
			groups.push(current_group)
			current_group = Queue()
		
		if is_groupable(current_group, student):
			current_group.enqueue(student)
		else:
			rejected.enqueue(student)

	#print(f"{current_group.size()} and {maxmem}")

	if current_group.size() != maxmem:
		while not current_group.is_empty():
			rejected.enqueue(current_group.dequeue())
	else:
		while not current_group.is_empty():
			groups.push(current_group)
			current_group.dequeue()
      
	# Print groups
	print_result = Stack()

	# Reverse the group order back using a second stack
	while not groups.is_empty():
		print_result.push(groups.pop())

	group_number = 1
	while not print_result.is_empty():
		group : Queue = print_result.pop()
  
		print(f"Group {group_number} : ",end='')
		while not group.is_empty():
			print(group.dequeue(), end='')
			print(', ', end='') if not group.is_empty() else print('', end='\n')
  
		group_number += 1

	# Print rejected
	if rejected.is_empty():
		print("Rejected : None")
	else:
		print("Rejected : ", end='')
		while not rejected.is_empty():
			print(rejected.dequeue(), end='')
			print(', ', end='') if not rejected.is_empty() else print('', end='')

main()