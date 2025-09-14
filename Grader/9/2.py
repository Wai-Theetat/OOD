class SortAlgorithm:
	def	SelectionSort(data : list) -> list:
		lst = data.copy()
  
		for i in range(0, len(lst) - 1):
			lowest_val_index = i
			for j in range(i + 1, len(lst)):
				if lst[j] < lst[lowest_val_index]:
					lowest_val_index = j
			lst[i], lst[lowest_val_index] = lst[lowest_val_index], lst[i]
		return lst

class Solution:
	def	main(self):
		nums = list(map(int, input('Enter Input : ').split()))
        
		pos_nums = []
		for a in nums:
			if a >= 0:
				pos_nums.append(a)
    
		sorted_pos_nums = SortAlgorithm.SelectionSort(pos_nums) 

		#print(sorted_pos_nums)

		for i in range(0, len(nums)):
			if nums[i] < 0:
				sorted_pos_nums.insert(i, nums[i])
				#print(sorted_pos_nums)
  
		for a in sorted_pos_nums:
			print(a, end=' ')
    
sol = Solution()
sol.main()