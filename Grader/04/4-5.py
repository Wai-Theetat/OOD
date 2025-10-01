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
    
    def copy_to_list(self):
        return self.__items.copy()

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

def think_mirror(mirror_str, item_queue):
	mirror_stack = Stack()
	exploded = 0

	#reverese
	mirror_str = mirror_str[::-1]

	for c in mirror_str:
		mirror_stack.push(c)
		while mirror_stack.size() >= 3:
			temp = mirror_stack.copy_to_list()
			if temp[-1] == temp[-2] == temp[-3]:
				mid = temp[-2]
				for _ in range(3):
					mirror_stack.pop()
				item_queue.enqueue(mid)
				exploded += 1
			else:
				break
	result = mirror_stack.copy_to_list()
	return result, exploded

def think_normal(normal_str, item_queue : Queue):
	normal_stack = Stack()
	exploded = 0
	failed_interrupt = 0

	for c in normal_str:
		normal_stack.push(c)
		
		while normal_stack.size() >= 3:
			temp = normal_stack.copy_to_list()
			
			if temp[-1] == temp[-2] == temp[-3]:
				if not item_queue.is_empty():
					last = normal_stack.pop()
					item = item_queue.dequeue()
					temp[-1] = item
					normal_stack.push(item)
					if  temp[-1] == temp[-2] == temp[-3]:
						for _ in range(3):
							normal_stack.pop()
						failed_interrupt += 1
					normal_stack.push(last)
     
				else:
					exploded += 1
					for _ in range(3):
							normal_stack.pop()
			else:
				break
			
	res = normal_stack.copy_to_list()
	return res, exploded, failed_interrupt


def main():
	normal_str, mirror_str = input("Enter Input (Normal, Mirror) : ").split()

	item_queue = Queue()

	mirror_result, mirror_exploded = think_mirror(mirror_str, item_queue)

	normal_result, normal_exploded, failed_interrupt = think_normal(normal_str, item_queue)
	
	#print(f"mirror_result = {mirror_result}, explode = {mirror_exploded}, item = {item_queue}")
	#print(f"normal_result = {normal_result}, explode = {normal_exploded}, item = {item_queue}, failed = {failed_interrupt}")
    
	print("NORMAL :")

	if len(normal_result) == 0:
		print("0\nEmpty")
	else:
		print(f"{len(normal_result)}")
		print(f"{''.join(normal_result[::-1])}")
  
	print(f"{normal_exploded} Explosive(s) ! ! ! (NORMAL)")

	if failed_interrupt > 0:
		print(f"Failed Interrupted {failed_interrupt} Bomb(s)")

	print("------------MIRROR------------")

	print(": RORRIM")
 
	if len(mirror_result) == 0:
		print("0\nytpmE")
	else:
		print(f"{len(mirror_result)}")
		print(f"{''.join(mirror_result[::-1])}")
  
	print(f"(RORRIM) ! ! ! (s)evisolpxE {mirror_exploded}")
	
    
main()