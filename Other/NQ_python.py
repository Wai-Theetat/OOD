def printBoard(b):
    print(b)

def putQueen(r, b, colFree, upFree, downFree):
	global N
	global numSol
	for c in range(N):
		if colFree[c] and upFree[r+c] and downFree[r-c+N-1]:
			b[r] = c
			colFree[c] = upFree[r+c] = downFree[r-c+N-1] = 0
			if r == N-1:
				printBoard(b)
				numSol += 1
			else:
				putQueen(r+1, b, colFree, upFree, downFree)
			colFree[c] = upFree[r+c] = downFree[r-c+N-1] = 1
 
N = 8
numSol = 0
b = N*[-1] # indices = rows, b[index] = coloumn, first init to -1
colFree = N*[1] # all N col are free at first
upFree = (2*N - 1)*[1] # all up diagonals are free at first
downFree = (2*N - 1)*[1] # all down diagonals are free at first
putQueen(0, b, colFree, upFree, downFree) # first add at 1st (ie. row 0)
print('number of solutions = ', numSol)