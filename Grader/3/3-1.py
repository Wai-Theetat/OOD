class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        popped = self.top.value
        self.top = self.top.next
        self._size -= 1
        return popped

    def peek(self):
        if self.is_empty():
            return None
        return self.top.value

    def is_empty(self):
        return self.top is None

    def size(self):
        return self._size


def is_pushable(ni, ns):
	res_p = ni + ns
	res_m = abs(ni - ns)

	if res_p == 10 or res_p == 5 or res_m == 10 or res_m == 5:
		return True
	else:
		return False
 

def main():
	stack = Stack()
	print("***Always 5 or 10***")

	num = [int(i) for i in input("Enter Input : ").split()]
	n_len = len(num)
	
	if n_len <= 0:
		return

	print("Output : ", end='')

	i = 0
	stack.push(num[i])
	print(num[i], end='')
	if(i+1 < n_len):
		print(" ", end='')
	i += 1

	while i < n_len:
		if is_pushable(num[i], stack.peek()):
			stack.push(num[i])
			print(num[i], end='')
			if(i+1 < n_len):
				print(" ", end='')
		i+=1

main()
