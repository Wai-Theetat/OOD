def flow(terrain, mx_r, mx_c, current_row, current_col):
	current_height = terrain[current_row][current_col]
	terrain[current_row][current_col] = 0

	if current_row - 1 >= 0 and terrain[current_row - 1][current_col] and terrain[current_row - 1][current_col] <= current_height:
		flow(terrain, mx_r, mx_c, current_row - 1, current_col)

	if current_col + 1 < mx_c and terrain[current_row][current_col + 1] and terrain[current_row][current_col + 1] <= current_height:
		flow(terrain, mx_r, mx_c, current_row, current_col + 1)

	if current_row + 1 < mx_r and terrain[current_row + 1][current_col] and terrain[current_row + 1][current_col] <= current_height:
		flow(terrain, mx_r, mx_c, current_row + 1, current_col)

	if current_col - 1 >= 0 and terrain[current_row][current_col - 1] and terrain[current_row][current_col - 1] <= current_height:
		flow(terrain, mx_r, mx_c, current_row, current_col - 1)

	return terrain

def build_terrain(rows, cols, data, i=0, terrain=None):
	if terrain is None:
		terrain = []
	if i == rows:
		return terrain
	row_data = list(map(int, list(data[i])))
	return build_terrain(rows, cols, data, i + 1, terrain + [row_data])

def print_line(lst_num, i=0):
    if i == len(lst_num): 
        print()
        return
    print(lst_num[i], end='')
    print_line(lst_num, i+1)

def print_terrain(terrain, i=0):
	if i == len(terrain):
		return
	print_line(terrain[i])
	print_terrain(terrain, i + 1)

def main():
	print(" *** Water Flow ***")
	raw_size, raw_data, start_pos = input("Input rows,cols/data1,data2,.../start_row,start_col : ").split('/')

	mx_r, mx_c = map(int, raw_size.split(','))
	data_rows = raw_data.split(',')

	terrain = build_terrain(mx_r, mx_c, data_rows)

	start_row, start_col = map(int, start_pos.split(','))

	if not ((1 <= mx_c <= 9) and (1 <= mx_r <= 9)):
		print('Error: Rows and columns must be between 1 and 9')
		return
	elif not (((0 <= start_col < mx_c) and (0 <= start_row < mx_r))):
		print('Error: Start coordinates are out of grid bounds')
		return

	new_terrain = flow(terrain, mx_r, mx_c, start_row, start_col)
	print_terrain(new_terrain)

main()
