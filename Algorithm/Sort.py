class SortAlgorithm:
	def	BubbleSort(data : list):
		lst = data.copy()
		swapped = True
  
		while swapped:
			swapped = False
			for i in range(0, len(lst) - 1):
				if lst[i] > lst[i+1]:
					swapped = True
					lst[i], lst[i+1] = lst[i+1], lst[i]
		return lst

	def	SelectionSort(data : list):
		lst = data.copy()
  
		for i in range(0, len(lst) - 1):
			lowest_val_index = i
			for j in range(i + 1, len(lst)):
				if lst[j] < lst[lowest_val_index]:
					lowest_val_index = j
			lst[i], lst[lowest_val_index] = lst[lowest_val_index], lst[i]
		return lst

	def	InsertionSort(data: list):
		lst = data.copy()

		for i in range(1, len(lst)): #from index 1 to last index
			iEle = lst[i] #assign insertElement
			for j in range(i, -1, -1):
				if j > 0 and lst[j-1] > iEle :
					lst[j] = lst[j-1]
				else:
					lst[j] = iEle	
					break
			#print(lst)
		return lst

	#Diminishing Increment Sort
	def	ShellSort(data: list, Diminishing : list):
		l = data.copy()
		
		for inc in Diminishing:
			for i in range(inc,len(l)): #insertion sort
				iEle = l[i] #inserting element
				for j in range(i, -1, -inc):
					if l[j-inc] > iEle and j >= inc:
						l[j] = l[j-inc]
					else:
						l[j] = iEle
						break
		return l
			
	def HeapSort(data : list):
		pass

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
		left = SortAlgorithm.MergeSort(data[:mid])
		right = SortAlgorithm.MergeSort(data[mid:])
		return merge(left, right)

	def QuickSort(data: list):
		def _think(arr, low, high):
			if low < high:
				# Partition the array
				pi = partition(arr, low, high)
				# Recursively sort left and right halves
				_think(arr, low, pi - 1)
				_think(arr, pi + 1, high)
			return arr

		def partition(arr, low, high):
			pivot = arr[high]  # last element as pivot
			i = low - 1
			for j in range(low, high):
				if arr[j] <= pivot:
					i += 1
					arr[i], arr[j] = arr[j], arr[i]
			arr[i + 1], arr[high] = arr[high], arr[i + 1]
			return i + 1
			
		if data is None: return None
		return _think(data.copy(), 0, len(data) - 1)


my_data = [32,26,2,15,264,-183,10,0,20,-142,-1]

print(f"Bubble Sort\t{SortAlgorithm.BubbleSort(my_data)}")
print(f"Selection Sort\t{SortAlgorithm.SelectionSort(my_data)}")	
print(f"Insertion Sort\t{SortAlgorithm.InsertionSort(my_data)}")
print(f"ShellSort Sort\t{SortAlgorithm.ShellSort(my_data, [1, 8, 23])}")
#print(f"Heap Sort\t{SortAlgorithm.HeapSort(my_data)}")
#print(f"Merge Sort\t{SortAlgorithm.MergeSort(my_data)}")
print(f"Quick Sort\t{SortAlgorithm.QuickSort(my_data)}")