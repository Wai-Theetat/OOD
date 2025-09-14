class Solution:
	def	main(self):
		nums = list(map(int, input('Enter Input : ').split()))
  
		is_ascended = True
		is_decended = True
		i = 0
		
		while (i < len(nums) - 1):
			if nums[i] <= nums[i + 1]:
				is_decended = False
			if nums[i] > nums[i + 1]:
				is_ascended = False
    
			i += 1

		if is_ascended or is_decended:
			print('Yes')
		else:
			print('No')

sol = Solution()
sol.main()