class Solution:
	def main(self):
		raw_nums, target = input("Enter Input : ").split('/')
		nums = list(map(float, raw_nums.strip().split()))
		target = float(target)
		n = len(nums)

		if not self.is_sorted(nums):
			return

		if target < nums[0]:
			index = -1
			percentile = 0
		elif target > nums[-1]:
			index = 999
			percentile = 100
		else:
			index = self.binary_search_with_fraction(nums, target)
			percentile = (index + 1) * 100 / n


		if index == len(nums)-1: percentile = int(percentile)


		print(f"\nindex      :   {index}")
		print(f"percentile :   {percentile}")

	def is_sorted(self, nums):
		return all(nums[i] <= nums[i+1] for i in range(len(nums) - 1))

	def binary_search_with_fraction(self, nums, target):
		left = 0
		right = len(nums) - 1

		while left <= right:
			mid = (left + right) // 2
			if nums[mid] == target:
				return float(mid)
			elif nums[mid] < target:
				left = mid + 1
			else:
				right = mid - 1

		lower_index = right
		upper_index = left
		low_val = nums[lower_index]
		high_val = nums[upper_index]
		decimal = (target - low_val) / (high_val - low_val)
		# index = (high_val - low_val) * decimal + lower_index
		index = lower_index + decimal
		return index

sol = Solution()
sol.main()
