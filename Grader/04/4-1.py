class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.items[0]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


def main():
	raw = input("Enter Input : ").split(',')
	i = 0
	
	queue = Queue()

	for tmp in raw:
		if tmp.startswith('E '):
			val = tmp.split()[1]
			queue.enqueue(val)
			print(f"Add {val} index is {i}")
			i += 1
		elif tmp == 'D':
			if queue.is_empty():
				print('-1')
			else:
				val = queue.dequeue()
				i -= 1
				print(f"Pop {val} size in queue is {i}")

	if queue.is_empty():
		print("Empty")
	else:
		print(f"Number in Queue is :  {queue}")

main()