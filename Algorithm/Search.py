class SearchAlgorithm:
	#Unordered (LinearSearch)
	def SentinelSearch(arr, target):
		n = len(arr)
		arr.append(target)
		i = 0
		while arr[i] != target:
			i += 1
		arr.pop()
		if i < n:
			return i
		return -1

	def MoveToFrontHeuristicSearch(arr, target):
		for i in range(len(arr)):
			if arr[i] == target:
				if i != 0:
					arr.insert(0, arr.pop(i))
				return 0
		return -1

	def TranspositionHeuristicSearch(arr, target):
		for i in range(len(arr)):
			if arr[i] == target:
				if i > 0:
					arr[i], arr[i - 1] = arr[i - 1], arr[i]
					return i - 1
				return i
		return -1


	#Ordered
	def SequentialSearch(arr, target):
		for i in range(len(arr)):
			if arr[i] == target:
				return i
			elif arr[i] > target:
				break
		return -1

	def BinarySearch(arr, target):
		low = 0
		high = len(arr) - 1
		while low <= high:
			mid = (low + high) // 2
			if arr[mid] == target:
				return mid
			elif arr[mid] < target:
				low = mid + 1
			else:
				high = mid - 1
        return -1



