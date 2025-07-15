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

class Customer:
	def __init__(self, id, si, pi):
		self.__id = id
		self.__si = int(si)
		self.__pi = int(pi)
		self.__start_time = None
		self.__end_time = None
		self.__wait_time = 0 		#time to wait til get to order

	@property
	def id(self):
		return self.__id

	@property
	def si(self):
		return self.__si

	@property
	def pi(self):
		return self.__pi

	@property
	def start_time(self):
		return self.__start_time

	@property
	def end_time(self):
		return self.__end_time

	@property
	def wait_time(self):
		return self.__wait_time

	@start_time.setter
	def start_time(self, val):
		self.__start_time = val
  
	@end_time.setter
	def end_time(self, val):
		self.__end_time = val
  
	@wait_time.setter
	def wait_time(self, val):
		self.__wait_time = val

class Barista:
	def __init__(self):
		self.__available_time = 0

	@property
	def available_time(self):
		return self.__available_time

	@available_time.setter
	def available_time(self, val):
		self.__available_time = val

def main():
	print(' ***Cafe***')
	logs = input("Log : ").split('/')
    
	all_customers = []
    
	for i, log in enumerate(logs):
		si, pi = log.split(',')
		all_customers.append(Customer(i + 1, si, pi))
	
	queue = Queue()
	baristas = [Barista(), Barista()]
	time = 0
	result = []	
	waiting = []		#customer who have to wait til he can order
	done = []
 
	while len(done) < len(all_customers):
		
		#When on customer time
		for person in all_customers:
			if person.si == time:
				queue.enqueue(person)
  
		for barista in baristas:
			#if barista free
			if barista.available_time <= time and not queue.is_empty():
	
				person : Customer = queue.dequeue()
				person.start_time = time
				person.end_time	  = time + person.pi
				person.wait_time  = person.start_time - person.si

				barista.available_time = person.end_time
				result.append((person.end_time, person.id))
				done.append(person)
				waiting.append(person)

		time += 1

	result.sort()
 
	for time, id in result:
		print(f'Time {time} customer {id} get coffee')
	
	max_time : int 		= 0
	max_cust : Customer = None
 
	for p in waiting:
		if max_time < p.wait_time:
			max_cust = p
			max_time = p.wait_time
   
	if max_cust == None and max_time == 0:
		print('No waiting')
	else:
		print(f'The customer who waited the longest is : {max_cust.id}\nThe customer waited for {max_cust.wait_time} minutes')
   
main()