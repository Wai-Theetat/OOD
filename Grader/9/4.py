class Solution:
	def	main(self):
		l = [e for e in input("Enter Input : ").split()]
		if l[0] == 'EX':
			Ans = "merge sort"
			print("Extra Question : What is a suitable sort algorithm?")
			print("   Your Answer : "+Ans)
		else:
			nums=list(map(int, l))
			lst = []
			for i in range(len(nums)):
				lst.append(nums[i])
				median = self.find_median(lst.copy())
				print(f"list = {lst} : median = {median}")

	def find_median(self, data):
		n = len(data)
		data = SortAlgorithm.MergeSort(data)
  
		if n % 2 == 1:
			return float(data[n // 2])
		else:
			mid = n // 2
			return (data[mid - 1] + data[mid]) / 2.0

class SortAlgorithm:
	def MergeSort(data: list):
		def merge(left, right):
			result = []
			i = j = 0
			while i < len(left) and j < len(right):
				if left[i] <= right[j]:
					result.append(left[i])
					i += 1
				else:
					result.append(right[j])
					j += 1
			result.extend(left[i:])
			result.extend(right[j:])
			return result

		if len(data) <= 1:
			return data
		mid = len(data) // 2
		left =  SortAlgorithm.MergeSort(data[:mid])
		right = SortAlgorithm.MergeSort(data[mid:])
		return merge(left, right)


sol = Solution()
sol.main()