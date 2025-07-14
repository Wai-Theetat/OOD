class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

def main():
	print("*****Big leg on the right side*****")
	nums = list(map(int, input("Enter input: ").split()))
	
	n_len = len(nums)
	res = [-1] * n_len
	
	i = 1
	stack = Stack()
	
	print(f"Stack push {0} index of {nums[0]}")
	stack.push(nums[0])
	
	while i < n_len :
		if not stack.is_empty() and nums[i] > stack.peek() :
      
			print(f"input[{i}]({nums[i]}) is greater than input[top of stack]({stack.peek()})")
			print("Stack pop")
			
			res[nums.index(stack.pop())] = nums[i]
			print(f"Output: {res}")
  
		else :
			print(f"Stack push {i} index of {nums[i]}")
			stack.push(nums[i])
			i += 1
   
	print(f"Output: {res}")
main()
