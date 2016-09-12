import sys
from copy import copy, deepcopy

def generate_grid():
	grid = []
	for row in sys.stdin:
		line = []
		for j in range((len(row) - 1)):	#subtract 1 for \n char
			line.append(row[j])
		grid.append(line)
	return grid

def check_win(grid):
	length = len(grid)
	winners = []

	#check rows
	win = True
	for i in range(length):
		row_char = grid[i][0]
		for j in range(length):
			if grid[i][j] != row_char or grid[i][j] == '_':
				win = False
		if win == True:
			winners.append(row_char)

	#check cols
	win = True
	for i in range(length):
		col_char = grid[0][i]
		for j in range(length):
			if grid[j][i] != col_char or grid[j][i] == '_':
				win = False
		if win == True:
			winners.append(col_char)

	#check diagonal_1
	win = True
	corner = grid[0][0]
	for i in range(length):
		if grid[i][i] != corner or grid[i][i] == '_':
			win = False
	if win == True:
		winners.append(corner)

	#check diagonal_2
	win = True
	corner = grid[0][length - 1]
	for i in range(length):
		if grid[i][length - i - 1] != corner or grid[i][length - i - 1] == '_':
			win = False
	if win == True:
		winners.append(corner)

	#return output
	if not winners:
		return 'n' #no winning move
	if all(x == winners[0] for x in winners) == True:
		return winners[0] #winning character
	else:
		return 'd'	#draw

def print_grid(grid):
	for x in grid:
		print x
	print "\n"


def check_blank_tiles(grid, x1, y1, x2, y2, outcome):
	tile = grid[y2][x2]
	print "2tile is ", tile
	print "x is ", x2, "y is ", y2
	if tile == '_':
		grid[y2][x2] = 'x'
		if check_win(grid) == 'x':
			outcome.append(['x', x1, y1, x2, y2])
		grid[x2][y2] = 'o'
		if check_win(grid) == 'o':
			outcome.append(['o', x1, y1, x2, y2])
		if check_win(grid) == 'd':
			outcome.append(['d', x1, y1, x2, y2])

def shift(grid, y, x, direction):
	outcome = []
	copy_grid = deepcopy(grid)
	length = len(copy_grid)
	tile = copy_grid[y][x]
	print "tile is ", tile
	if direction == "left":
		for i in range(length - 1):
			copy_grid[y][i] = copy_grid[y][i + 1]
		copy_grid[y][i + 1] = tile
		check_blank_tiles(copy_grid, x, y, i + 1, y, outcome)
	if direction == "right":
		for i in range(length - 1):
			copy_grid[y][x - i] = copy_grid[y][x - i - 1]
			copy_grid[y][x - i - 1] = tile
			check_blank_tiles(copy_grid, x, y, x - i - 1, y, outcome)
	if direction == "up":
		for i in range(length - 1):
			copy_grid[i][x] = copy_grid[i + 1][x]
			copy_grid[i + 1][x] = tile
			check_blank_tiles(copy_grid, x, y, x, i + 1, outcome)
	if direction == "down":
		for i in range(length - 1):
			copy_grid[y - i][x] = copy_grid[y - i - 1][x]
			copy_grid[y - i - 1][x] = tile
			check_blank_tiles(copy_grid, x, y, x, y - i - 1, outcome)

	print_grid(copy_grid)
	# 	for i in range(length - 1):

	print outcome



#account for tile changing!!!
def search_moves(grid, i, j,):
	winning_moves = []
	length = len(grid)
	if j < length - 1:
		print "#1"
		print i, length - 1
		# print "in search move, tile is ", grid[i][j]
		shift(grid, i, j, "left")
	if j > 0:
		print '#2'
		print i, 0
		shift(grid, i, j, "right")
	if i < length - 1:
		print '#3'
		print length - 1, j
		shift(grid, i, j, "up")
	if i > 0:
		print '#4'
		print 0, j
		shift(grid, i, j, "down")

	return winning_moves


def brute_force(grid):
	length = len(grid)
	for i in range(length):
		for j in range(length):
			if i == 0 or j == 0 or i == length - 1 or j == length - 1:
				winning_moves = search_moves(grid, i, j)
	#output winning moves

def solve_quixo():
	grid = generate_grid()
	brute_force(grid)


solve_quixo()



	# #corner block
	# if (i == 0 and (j == 0 or j == len(grid) -1)) or \
	# 	 (i == len(grid) -1 and (j == 0 or j == len(grid) - 1)):
	# 	 print i, j

# lines = [line.split() for line in sys.stdin]
# grid = [['_' for x in range(len(lines))] for y in range(len(lines))]

#how to parse from textfile instead
#with open("textFile.txt") as textFile:
#   lines = [line.split() for line in textFile]

# def shift_up(grid, x, y):
# 	outcome = []
# 	copy_grid = deepcopy(grid)
# 	length = len(copy_grid)
# 	tile = copy_grid[x][y]
# 	for i in range(length - 1):
# 		copy_grid[i][y] = copy_grid[i + 1][y]
# 	copy_grid[i + 1][y] = tile
# 	outcome = check_blank_tiles(copy_grid, x, y, outcome)

# 	# if tile == '_':
# 	# 	copy_grid[x][y] = 'x'
# 	# 	if check_win(copy_grid) == 'x':
# 	# 		outcome.append(['x', x, y, i+1, y])
# 	# 		print copy_grid
# 	# 	copy_grid[x][y] = 'o'
# 	# 	if check_win(copy_grid) == 'o':
# 	# 		outcome.append(['o', x, y, i+1, y])
# 	# 	if check_win(copy_grid) == 'd':
# 	# 		outcome.append(['d', x, y, i+1, y])
# 	# print outcome