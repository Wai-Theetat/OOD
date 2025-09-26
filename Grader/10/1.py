class Solution:
	def main(self):
		raw_nums, target  = input("Enter Input:").split('/')
        
		target		= float(target)
		nums		= list(map(float,raw_nums.split()))
		index		= 0
		percentile	= 0

		if self.is_sorted(nums):

			if target > nums[len(nums)-1] : target = nums[len(nums)-1]
			elif target < nums[0]		  : target = nums[0]


			index		= self.binary_search(nums, target)
			percentile	= 0 



	def is_sorted(self, nums):
		if nums is None : return False
		a = nums[0]
		for n in nums:
			if n > a: return False
		return True

	def binary_search(self, nums, target):
		left = 0
		right = len(nums)-1

		while left <= right:
			mid = (left + right)//2

			if nums[mid] == target:
				return mid
			
			if nums[mid] <= target:
				left = mid + 1
			else:
				right = mid - 1
		return -1

sol = Solution();
sol.main()