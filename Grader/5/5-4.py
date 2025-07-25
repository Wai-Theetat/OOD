class Node:
	def __init__(self, value):
		self.__value = value
		self.__prev = None
		self.__next = None

	@property
	def value(self):
		return self.__value

	@value.setter
	def value(self, new_value):
		self.__value = new_value

	@property
	def next(self):
		return self.__next

	@next.setter
	def next(self, node):
		self.__next = node

	@property
	def prev(self):
		return self.__prev

	@prev.setter
	def prev(self, node):
		self.__prev = node

class LinkedList:
	def __init__(self):
		self.__head = None
		self.__tail = None
		self.__size = 0

	@property
	def head(self):
		return self.__head
	@property
	def size(self):
		return self.__size

	def is_empty(self):
		return self.__head is None

	def add_new_head(self, value):
		new_node = Node(value)
		new_node.next = self.__head

		if not self.is_empty():
			self.__head.prev = new_node
		else:
			self.__tail = new_node

		self.__head = new_node
		self.__size += 1
		return new_node

	def append(self, value):
		new_node = Node(value)

		if self.is_empty():
			self.__head = self.__tail = new_node
		else:
			self.__tail.next = new_node
			new_node.prev = self.__tail
			self.__tail = new_node

		self.__size += 1
		return new_node

	def insert(self, value, index):
		if index < 0 or index > self.__size:
			raise IndexError("Index out of bounds")
		if index == 0:
			return self.add_new_head(value)
		if index == self.__size:
			return self.append(value)

		new_node = Node(value)
		mid = self.__size // 2

		if index <= mid:
			current = self.__head
			for _ in range(index - 1):
				current = current.next
		else:
			current = self.__tail
			for _ in range(self.__size - index):
				current = current.prev

		new_node.next = current.next
		new_node.prev = current
		if current.next:
			current.next.prev = new_node
		current.next = new_node

		self.__size += 1
		return new_node

	def delete(self, index):
		if self.is_empty():
			raise IndexError("Remove from empty list")
		if index < 0 or index >= self.__size:
			raise IndexError("Index out of bounds")

		if index == 0:
			return self.delete_head()
		if index == self.__size - 1:
			return self.delete_tail()

		mid = self.__size // 2
		if index <= mid:
			current = self.__head
			for _ in range(index):
				current = current.next
		else:
			current = self.__tail
			for _ in range(self.__size - index - 1):
				current = current.prev

		current.prev.next = current.next
		current.next.prev = current.prev
		self.__size -= 1
		return current.value

	def delete_head(self):
		if self.is_empty():
			raise IndexError("Remove from empty list")

		removed_value = self.__head.value
		if self.__head == self.__tail:
			self.__head = self.__tail = None
		else:
			self.__head = self.__head.next
			self.__head.prev = None

		self.__size -= 1
		return removed_value

	def delete_tail(self): 
		if self.is_empty():
			raise IndexError("Remove from empty list")

		removed_value = self.__tail.value
		if self.__head == self.__tail:
			self.__head = self.__tail = None
		else:
			self.__tail = self.__tail.prev
			self.__tail.next = None

		self.__size -= 1
		return removed_value

	def index_of(self, value):
		current = self.__head
		index = 0
		while current:
			if current.value == value:
				return index
			current = current.next
			index += 1
		return -1

	def __str__(self):
		values = []
		current = self.__head
		while current:
			values.append(str(current.value))
			current = current.next
		return " ".join(values) if values else "Empty"

	def __getitem__(self, index):
		if index < 0:
			index += self.__size
		if index < 0 or index >= self.__size:
			raise IndexError("Index out of bounds")

		mid = self.__size // 2
		if index <= mid:
			current = self.__head
			for _ in range(index):
				current = current.next
		else:
			current = self.__tail
			for _ in range(self.__size - index - 1):
				current = current.prev

		return current.value

	def __setitem__(self, index, value):
		if index < 0:
			index += self.__size
		if index < 0 or index >= self.__size:
			raise IndexError("Index out of bounds")

		mid = self.__size // 2
		if index <= mid:
			current = self.__head
			for _ in range(index):
				current = current.next
		else:
			current = self.__tail
			for _ in range(self.__size - index - 1):
				current = current.prev

		current.value = value
  
	#clear all item of linked-list
	def clear(self):
		self.__head = self.__tail = None
		self.__size = 0

class Ant:
	def __init__(self, name):
		self.__name = name

	def __str__(self): 
		return self.__name

class WorkerAnt(Ant):
	def __init__(self, name):
		super().__init__(name)
		self.__carry  = 2
		self.__damage = 5
  
	@property
	def carry_power(self): return self.__carry
	@property
	def damage_power(self): return self.__damage

class ArmyAnt(Ant):
	def __init__(self, name):
		super().__init__(name)
		self.__carry  = 5
		self.__damage = 10

	@property
	def carry_power(self): return self.__carry
	@property
	def damage_power(self): return self.__damage

#เหล่ามดจะถูกจัดเก็บอยู่ใน linked list เดียวกัน
class Population(LinkedList):
	def __init__(self, worker, army):
		super().__init__()
  
		self.__latest_W_name = 0
		self.__latest_A_name = 0
  
		self.add_ant(worker, 'W')
		self.add_ant(army, 'A')

	
	def add_ant(self, amount, ant_type):
		for _ in range(amount):
			if ant_type == 'W':
				self.latest_W += 1
				name = f"W{self.latest_W}"
				ant = WorkerAnt(name)

				if self.is_empty():
					self.append(ant)
				else:
					head_val = self.head.value
					if isinstance(head_val, Ant):
						offset = int(str(head_val)[1:])
						self.insert(ant, self.latest_W - offset)
					else:
						self.append(ant)

			elif ant_type == 'A':
				self.latest_A += 1
				name = f"A{self.latest_A}"
				ant = ArmyAnt(name)
				self.append(ant)

	@property
	def latest_W(self): return self.__latest_W_name
	@property
	def latest_A(self): return self.__latest_A_name

	@latest_W.setter
	def latest_W(self, val): self.__latest_W_name = val
	@latest_A.setter
	def latest_A(self, val): self.__latest_A_name = val
 
#หากราชินีโกรธครบ 3 ครั้ง รังมดจะแตกและหยุดทำงานทันที
class Colony:
	def __init__(self, wp, ap):
		self.__angry = 0
		self.__ant_population = Population(wp, ap)
  
	@property
	def ant_population(self):
		return self.__ant_population

	@property
	def angry(self):
		return self.__angry

	@angry.setter
	def angry(self, val):
		self.__angry = val
  
	def collect_food(self, req_value):
		print("Food carrying mission :", end=" ")
		i = 0
		total = 0
		ant_available = False
		used = 0
  
		# Collect from WorkerAnts first
		while i < self.ant_population.size:
			ant = self.ant_population[i]

			print(ant, end='')
			total += ant.carry_power
			self.ant_population.delete(i)
			ant_available = True
			used += 1

			if total >= req_value:
				break
			else:
				print('',end=' ')
		
		if not ant_available:
			print("Empty", end="") 
		print()
  
		self.reset_if_needed()
  
		if total < req_value:
			print("The food load is incomplete!")
			self.angry += 1
			print("Queen is angry! ! !")
   
   
	def fight_enemy(self, hp):
		print("Attack mission :", end=" ")
		ant_available = False

		#start at index after worker which is ArmyAnts likely begin
		i = self.ant_population.latest_W
		while i < self.ant_population.size and hp > 0:
			ant = self.ant_population[i]
			if isinstance(ant, ArmyAnt):
				print(ant, end='')
				hp -= ant.damage_power
				self.ant_population.delete(i)
				ant_available = True
				if hp > 0:
					print('', end=' ')
			else:
				i += 1  # skip non-ArmyAnts

		# Fallback to WorkerAnts (start from beginning) if not enough ArmyAnts
		i = 0
		while i < self.ant_population.size and hp > 0:
			ant = self.ant_population[i]
			if isinstance(ant, WorkerAnt):
				print(ant, end='')
				hp -= ant.damage_power
				self.ant_population.delete(i)
				ant_available = True
				if hp > 0:
					print('', end=' ')
			else:
				i += 1

		if not ant_available:
			print("Empty", end='')
		print()

		self.reset_if_needed()

		if hp > 0:
			print("Ant nest has fallen!")
			return False
		return True


	def reset_if_needed(self):
		has_worker = False
		has_army = False

		for i in range(self.ant_population.size):
			ant = self.ant_population[i]
			if isinstance(ant, WorkerAnt):
				has_worker = True
			elif isinstance(ant, ArmyAnt):
				has_army = True

		if not has_worker:
			self.ant_population.latest_W = 0
		if not has_army:
			self.ant_population.latest_A = 0


   
def main():
	print("***This colony is our home***")
	raw_ant_population, raw_commands = input("Enter input : ").split('/')

	w_ant, a_ant = raw_ant_population.split() 
	colony = Colony(int(w_ant), int(a_ant))

	print(f"Current Ant List: {colony.ant_population}\n")	

	for command in raw_commands.split(','):
		tokens = command.strip().split()

		if tokens[0] == 'W':
			colony.ant_population.add_ant(int(tokens[1]), 'W')
			#print(f"Current Ant List: {colony.ant_population}")

		elif tokens[0] == 'A':
			colony.ant_population.add_ant(int(tokens[1]), 'A')
			#print(f"Current Ant List: {colony.ant_population}")

		elif tokens[0] == 'C':
			colony.collect_food(int(tokens[1]))
			if colony.angry >= 3:
				print("**The queen is furious! The ant colony has been destroyed**")
				break

		elif tokens[0] == 'F':
			success = colony.fight_enemy(int(tokens[1]))
			if not success:
				colony.angry += 1
				if colony.angry >= 3:
					print("**The queen is furious! The ant colony has been destroyed**")
				break


		elif tokens[0] == 'S':
			print("-> Remaining worker ants:", end=' ')
			has_worker = False
			for i in range(colony.ant_population.size):
				ant = colony.ant_population[i]
				if isinstance(ant, WorkerAnt):
					print(ant, end=' ')
					has_worker = True
			if not has_worker:
				print("Empty", end='')
			print()

			print("-> Remaining soldier ants:", end=' ')
			has_army = False
			for i in range(colony.ant_population.size):
				ant = colony.ant_population[i]
				if isinstance(ant, ArmyAnt):
					print(ant, end=' ')
					has_army = True
			if not has_army:
				print("Empty", end='')
			print()

main()