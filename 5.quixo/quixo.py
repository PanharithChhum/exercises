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

	# print "check rows"
	for i in range(length):
		win = True
		row_char = grid[i][0]
		for j in range(length):
			# print "grid[",i,"][",j,"] is ", grid[i][j]
			if grid[i][j] != row_char or grid[i][j] == '_':
				win = False
		# print win
		if win == True:
			winners.append(row_char)

	# print "check cols"
	for i in range(length):
		win = True
		col_char = grid[0][i]
		for j in range(length):
			# print "grid[",i,"][",j,"] is ", grid[j][i]
			if grid[j][i] != col_char or grid[j][i] == '_':
				win = False
		# print win
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

#check win without blank tiles too!!!
def check_blank_tiles(grid, x1, y1, x2, y2, outcome):
	if check_win(grid) == 'x':
		outcome.append(['x', x1, y1, x2, y2])
	if check_win(grid) == 'o':
		outcome.append(['o', x1, y1, x2, y2])
	if check_win(grid) == 'd':
		outcome.append(['d', x1, y1, x2, y2])
		
	print "x1:", x1, " y1:", y1, " x2:", x2, " y2", y2
	print "tile is ", grid[y2][x2]
	tile = grid[y2][x2]
	if tile == '_':
		grid[y2][x2] = 'x'
		if check_win(grid) == 'x':
			outcome.append(['x', x1, y1, x2, y2])
		grid[y2][x2] = 'o'
		if check_win(grid) == 'o':
			outcome.append(['o', x1, y1, x2, y2])
		if check_win(grid) == 'd':
			outcome.append(['d', x1, y1, x2, y2])
	print outcome

def shift(grid, y, x, direction, outcome):
	length = len(grid)
	tile = grid[y][x]
	temp = 0
	print "tile is ", tile
	# if direction == "left":
	# 	copy_grid = deepcopy(grid)
	# 	print "goin left"
	# 	for i in range(x, length - 1):
	# 		print y, i, copy_grid[y][i], " gets ", y, i + 1, copy_grid[y][i + 1]
	# 		copy_grid[y][i] = copy_grid[y][i + 1]
	# 	copy_grid[y][length - 1] = tile
	# 	print_grid(copy_grid)
	# 	check_blank_tiles(copy_grid, x, y, length - 1, y, outcome)
	# if direction == "right":
	# 	copy_grid = deepcopy(grid)
	# 	print "goin right"
	# 	for i in reversed(range(1, x + 1)):
	# 		print y, i, copy_grid[y][i], " gets ", y, i-1, copy_grid[y][i - 1]
	# 		copy_grid[y][i] = copy_grid[y][i - 1]
	# 	copy_grid[y][0] = tile
	# 	print_grid(copy_grid)
	# 	check_blank_tiles(copy_grid, x, y, 0, y, outcome)
	# if direction == "up":
	# 	print "goin up"
	# 	copy_grid = deepcopy(grid)
	# 	for i in range(y, length - 1):
	# 		print i, x, copy_grid[i][x], " gets ", i + 1, x, copy_grid[i+1][x]
	# 		copy_grid[i][x] = copy_grid[i + 1][x]
	# 	copy_grid[length - 1][x] = tile
	# 	print_grid(copy_grid)
	# 	check_blank_tiles(copy_grid, x, y, x, length - 1, outcome)
	# 	print outcome
	if direction == "down":
		print "goin down"
		copy_grid = deepcopy(grid)
		for i in reversed(range(1, y + 1)):
			copy_grid[i][x] = copy_grid[i-1][x]
		copy_grid[0][x] = tile
		print_grid(copy_grid)
		check_blank_tiles(copy_grid, x, y, x, 0, outcome)

def search_moves(grid, i, j,):
	winning_moves = []
	length = len(grid)
	# if j < length - 1:
	# 	shift(grid, i, j, "left", winning_moves)
	# if j > 0:
	# 	shift(grid, i, j, "right", winning_moves)
	# if i < length - 1:
	# 	shift(grid, i, j, "up", winning_moves)
	if i > 0:
		shift(grid, i, j, "down", winning_moves)

	return winning_moves


def brute_force(grid):
	length = len(grid)
	for i in range(length):
		for j in range(length):
			if i == 0 or j == 0 or i == length - 1 or j == length - 1:
				return search_moves(grid, i, j)

def print_formatted(winning_moves):
	for move in winning_moves:
		table = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E'}
		print move[0], table[move[1]], move[2]+1, " -> ", table[move[3]], move[4]+1

def solve_quixo():
	grid = generate_grid()
	print_grid(grid)
	# print check_win(grid)
	search_moves(grid, 4, 4)
	# winning_moves = brute_force(grid)
	# print_formatted(winning_moves)

solve_quixo()

