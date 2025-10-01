class TorKham:
	def __init__(self):
		self.words = []

	def restart(self):
		self.words.clear()
		print("game restarted")
 
	def play(self, word : str):
		if (word.startswith("P ")):
			word = word[2:]
			if self.check_match(word):	
				self.words.append(word)
				self.mt_print_list(word)
			else:
				self.mt_print_err(word, 1)

		elif (word == "R"):
			self.restart()

		elif (word == "X"):
			return 0
		else :
			self.mt_print_err(word, 2)
			return 0
		return 1

	def	check_match(self, word):
		if not self.words:
			return 1
		previous_word = self.words[-1]
		if word[0].lower() == previous_word[-2].lower() and word[1].lower() == previous_word[-1].lower():
			return 1
		else:
			return 0

	def	mt_print_list(self, word):
		print(f"'{word}' -> {self.words}")

	def	mt_print_err(self, word, errtype):
		if errtype == 1:
			print(f"'{word}' -> game over")
		if errtype == 2:
			print(f"'{word}' is Invalid Input !!!")

torkham = TorKham()
print("*** TorKham HanSaa ***")
S = input("Enter Input : ").split(',')

for word in S:
    if not torkham.play(word):
        break