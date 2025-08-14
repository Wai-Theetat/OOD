def formatAlpN(st, index = 0):
	n = len(st)
	if index < n:
		if not st[index].isalnum():
			st = st.replace(st[index], "")
		
		return formatAlpN(st, index+1)
	else:
		return st

def	isPalin(txt, fst, lst):

	if txt[fst] != txt[lst]: return False
	
	elif fst > lst: return True

	else: return isPalin(txt, fst + 1, lst - 1)

def main():
	print("**Palindrome pretty version!**")
	
	raw = input("Enter message : ").lower()

	txt = formatAlpN(raw)

	print(isPalin(txt, 0, len(txt)-1))

main()

