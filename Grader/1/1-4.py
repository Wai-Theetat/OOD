def draw_spiral(n):
    size = 4 * n - 3
    grid = [['.' for _ in range(size)] for _ in range(size)]

    for layer in range(0, size, 2):
        end = size - layer - 1
        if layer > end:
            break
        # top
        for i in range(layer, end + 1):
            grid[layer][i] = '#'
        # left
        for i in range(end - 1, layer, -1):
            grid[i][layer] = '#'
        # right
        for i in range(layer + 1, end + 1):
            grid[i][end] = '#'
        # bottom
        for i in range(end - 1, layer - 1, -1):
            grid[end][i] = '#'
       

    for row in grid:
        print(''.join(row))

n = int(input("*** Fun with Drawing ***\nEnter input : "))
draw_spiral(n)
