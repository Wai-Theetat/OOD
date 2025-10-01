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

def main():
	raw = input("input : ").split(',')
	
	queue = Queue()
	err_inp_cnt = 0	
	err_deq_cnt = 0
	i = 0
 
	for step in raw:
		
		print(f"Step : {step}")

		if step.startswith("D") and step[1:].isdigit():
			val = int(step[1:])
			qsize = queue.size()

			if qsize < val:
				err_deq_cnt += val - qsize
				for _ in range(0, qsize):
					queue.dequeue()
			else:
				for _ in range(0, val):
					queue.dequeue()

			print(f"Dequeue : {queue}")
   
		elif step.startswith("E") and step[1:].isdigit():
			val = int(step[1:])
			qsize = queue.size()

			for _ in range(0, val):
				queue.enqueue(f'*{i}')
				i += 1
    
			print(f"Enqueue : {queue}")
   
		else:
			print(queue)
			err_inp_cnt += 1

		print(f"Error Dequeue : {err_deq_cnt}")
		print(f"Error input : {err_inp_cnt}")
		print(f"--------------------")

main()