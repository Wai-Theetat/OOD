class Soulution:
	def main(self):
		print("This is your BOOK!!!")
		shelfs, borrows = input("Enter input: ").split('/')
		
		shelfs	= shelfs.split()
		borrows	= borrows.split()
		counter	= []
		cost 	= 0

		while borrows:
			found  = False
			wanted = borrows.pop(0)
			for i in range(0, len(shelfs)):
				#Found
				if shelfs[i] == wanted:
					cost += i+1

					shelfs.insert(0, shelfs.pop(i))
					print(f"Search {wanted} -> found at {i+1} move to front -> ", end=' ')
					self.printlst(shelfs)
					print()

					found = True
					break

			if found : continue

			#Not Found
			for b in range(0, len(counter)):
				if counter[b] == wanted:
					book = counter.pop(b)
					shelfs.insert(0, book)

					print(f"Search {wanted} -> add new book -> ", end=' ')
					self.printlst(shelfs)
					print()

					cost += 1
					found = True
					break
			
			if found : continue

			counter.append(wanted)

			print(f"Search {wanted} -> not found ->", end=' ')
			self.printlst(shelfs)
			print()
			
			cost += len(shelfs)+1

		print("\nFinal books: ", end='')
		self.printlst(shelfs)
		print()
		print("Total cost:", cost)


	def printlst(self, lst):
		for i in range(0, len(lst)):

			if i < len(lst)-1:
				print(lst[i], end=' ')
			else:
				print(lst[i], end='')

sol = Soulution()
sol.main()