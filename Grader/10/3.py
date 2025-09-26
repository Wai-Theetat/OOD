class Data:
	def __init__(self, key, value):
		self.key = key
		self.value = value
	def __str__(self):
		return "({0}, {1})".format(self.key, self.value)

class Solution:
	def main(self):
		print(" ***** Fun with hashing *****")
		raw_value, raw_data = input("Enter Input : ").split('/')

		hash_table		= []
		max_t_size		= int(raw_value.split()[0])
		max_chain_c		= int(raw_value.split()[1])
		full_data		= []

		for data in raw_data.split(','):
			full_data.append(Data(data.split()[0], data.split()[1]))
			# print(full_data[len(full_data)-1])

		for _ in range(0, max_t_size) : hash_table.append(None)

		i = 0
		while full_data or max_t_size:
			before_hash = full_data[i].key
			hashed		= self.hashing(before_hash)


sol = Solution()
sol.main()