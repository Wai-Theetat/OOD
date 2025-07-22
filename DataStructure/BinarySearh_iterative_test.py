class Node:
	def __init__(self, data):
		self.__left		= None
		self.__right	= None
		self.__data		= data
  
	@property
	def left(self):
		return self.__left

	@property
	def right(self):
		return self.__right

	@property
	def data(self):
		return self.__data

	@left.setter
	def left(self, value):
		self.__left = value
  
	@right.setter
	def right(self, value):
		self.__right = value
  
def searchI(l, h, val, nums):
    
	while h > l:
		m = (l+h)//2
		if val == nums[m]:
			return m
		elif val > nums[m]:
			l = m + 1
		else:
			h = m - 1
	return None
nums = [1,3,2,93,2,23,89,433]
nums.sort()

print(nums)

n = 17
ans = f"found first {n} at index : {searchI(0, len(nums)-1, n, nums)}"

print(ans)
  
  
