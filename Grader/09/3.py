class Solution:
	def main(self):
		raws = input('Enter Input : ').split(',')
		products = []
		for item in raws:
			n = str(item.split()[0])
			p = int(item.split()[1])
			products.append(Item(n, p))
		self.sort_item(products.copy())

	def sort_item(self, data):
		print("----------------------------------------")
		print("Sort by price :")
		self.quick_sort(data, 1)
		self.print_items(data)
		print("----------------------------------------")
		print("Sort by price and alphabet :")
		data = self.sort_name(data)
		self.print_items(data)

	def print_items(self, data):
		for i, item in enumerate(data):
			print(f"{i+1:>2}. {item.name():<12}{item.price():>4}")

	def sort_name(self, lst):
		dis_g = self.distribute_group(lst)
		for sub_group in dis_g:
			self.quick_sort(sub_group, 2)
		return self.merge_distribute_group(dis_g)

	def distribute_group(self, lst):
		res = []
		for item in lst:
			p = False
			for group in res:
				if group[0].price() == item.price():
					group.append(item)
					p = True
					break
			if not p:
				res.append([item])
		return res

	def merge_distribute_group(self, lst):
		res = []
		for lst_item in lst:
			for item in lst_item:
				res.append(item)
		return res

	def quick_sort(self, lst, mode):
		self._quick_sort(lst, 0, len(lst) - 1, mode)

	def _quick_sort(self, lst, low, high, mode):
		if low < high:
			pv = self._partition(lst, low, high, mode)
			self._quick_sort(lst, low, pv - 1, mode)
			self._quick_sort(lst, pv + 1, high, mode)

	def _partition(self, lst, low, high, mode):
		pivot = lst[low]
		start = low + 1
		end = high
		while True:
			while (start <= end and
				   ((mode == 1 and lst[end].price() >= pivot.price()) or
					(mode == 2 and self.string_compare(lst[start].name(), pivot.name()) == 2))):
				end -= 1
			while (start <= end and
				   ((mode == 1 and lst[start].price() <= pivot.price()) or
					(mode == 2 and self.string_compare(lst[start].name(), pivot.name()) == 0))):
				start += 1
			if start <= end:
				lst = self.swap(lst, start, end)
			else:
				break
		lst = self.swap(lst, low, end)
		return end

	def swap(self, lst, a, b):
		temp = lst[a]
		lst[a] = lst[b]
		lst[b] = temp
		return lst

	def string_compare(self, str1, str2):
		i = 0
		j = 0
		while i < len(str1) and j < len(str2):
			if str1[i] > str2[j]:
				return 2
			elif str1[i] < str2[j]:
				return 0
			i += 1
			j += 1
		if i == len(str1) and j < len(str2):
			return 0
		elif i < len(str1) and j == len(str2):
			return 2
		return 1


class Item:
	def __init__(self, name, price):
		self.__name = name
		self.__price = price

	def name(self):
		return self.__name

	def price(self):
		return self.__price


s = Solution()
s.main()
