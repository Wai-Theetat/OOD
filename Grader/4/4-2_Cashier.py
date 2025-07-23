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
	raw = input('Enter people and time : ')
	raw_waiting, minute = raw.split()	
	
	waiting = Queue()
	cashier_1 = Queue()
	cashier_2 = Queue()
	minute = int(minute)	

	time1 = 3
	time2 = 2

	for run in raw_waiting:
		waiting.enqueue(run)

	for i in range(1, minute+1):
		
		customer = None
		if not waiting.is_empty():
			customer = waiting.dequeue()
		
		if time1 == 0:
			cashier_1.dequeue()
			time1 = 3
		if time2 == 0:
			cashier_2.dequeue()
			time2 = 2
  
		if cashier_1.size() < 5 and customer is not None:
			cashier_1.enqueue(customer)
		elif cashier_2.size() < 5 and customer is not None:
			cashier_2.enqueue(customer)

		if not cashier_1.is_empty():
			time1 -= 1
		if not cashier_2.is_empty():
			time2 -= 1

		print(f"{i} {waiting} {cashier_1} {cashier_2}")

main()
