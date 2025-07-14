def	ft_draw(n):
	size = 2 * n + 4
	grid = [['.' for _ in range(size)] for _ in range(size)]
	
	#top left
	for i in range(0, int(size/2)):
		for j in range(0, int(size/2)):
			grid[i][j] = '#' if i+j > n else '.'

	#bottom right
	for i in range(int(size/2), size):
		for j in range(int(size/2), size):
			grid[i][j] = '+' if i + j <= 2*size - int(size/2) - 1 else '.'
   
   #top right
	for i in range(0, int(size/2)):
		for j in range(int(size/2), size):
			grid[i][j] = '+' if	i == 0 or i == int(size/2) - 1 or j == int(size/2) or j == size - 1 else '#'  

   #bottom left
	for i in range(int(size/2), size):
		for j in range(0, int(size/2)):
			grid[i][j] = '#' if	j == 0 or j == int(size/2) - 1 or i == int(size/2) or i == size - 1 else '+' 

	for row in grid:
		print(''.join(row))

n = int(input("Enter Input : "))
ft_draw(n)