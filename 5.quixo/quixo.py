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

def check_win(grid, outcome, x1, y1, x2, y2):
	length = len(grid)
	winners = []

	# print "check rows"
	for i in range(length):
		win = True
		row_char = grid[i][0]
		for j in range(length):
			if grid[i][j] != row_char or grid[i][j] == '_':
				win = False
		if win == True:
			winners.append(row_char)

	# print "check cols"
	for i in range(length):
		win = True
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

	#output
	if not winners:
		return
	if all(x == winners[0] for x in winners) == True:
		win = [winners[0], x1, y1, x2, y2]
		if win not in outcome:
			outcome.append(win)
	else:
		draw = ['d', x1, y1, x2, y2]
		if draw not in outcome:
			outcome.append(draw)

#prints formatted grid for debugging
def print_grid(grid):
	for x in grid:
		print x
	print "\n"

#analyzes board for win and accounts for blank tiles
def analyze_board(grid, x1, y1, x2, y2, outcome):
		
	check_win(grid, outcome, x1, y1, x2, y2)
	tile = grid[y2][x2]
	if tile == '_':
		grid[y2][x2] = 'x'
		check_win(grid, outcome, x1, y1, x2, y2)
		grid[y2][x2] = 'o'
		check_win(grid, outcome, x1, y1, x2, y2)

def shift(grid, y, x, direction, outcome):
	length = len(grid)
	tile = grid[y][x]

	if direction == "left":
		copy_grid = deepcopy(grid)
		for i in range(x, length - 1):
			copy_grid[y][i] = copy_grid[y][i + 1]
		copy_grid[y][length - 1] = tile
		analyze_board(copy_grid, x, y, length - 1, y, outcome)
	
	if direction == "right":
		copy_grid = deepcopy(grid)
		for i in reversed(range(1, x + 1)):
			copy_grid[y][i] = copy_grid[y][i - 1]
		copy_grid[y][0] = tile
		analyze_board(copy_grid, x, y, 0, y, outcome)
	
	if direction == "up":
		copy_grid = deepcopy(grid)
		for i in range(y, length - 1):
			copy_grid[i][x] = copy_grid[i + 1][x]
		copy_grid[length - 1][x] = tile
		analyze_board(copy_grid, x, y, x, length - 1, outcome)
	
	if direction == "down":
		copy_grid = deepcopy(grid)
		for i in reversed(range(1, y + 1)):
			copy_grid[i][x] = copy_grid[i-1][x]
		copy_grid[0][x] = tile
		analyze_board(copy_grid, x, y, x, 0, outcome)

def search_moves(grid, i, j, winning_moves):
	length = len(grid)
	if j < length - 1:
		shift(grid, i, j, "left", winning_moves)
	if j > 0:
		shift(grid, i, j, "right", winning_moves)
	if i < length - 1:
		shift(grid, i, j, "up", winning_moves)
	if i > 0:
		shift(grid, i, j, "down", winning_moves)

	return winning_moves


def brute_force(grid):
	winning_moves = []
	length = len(grid)
	for i in range(length):
		for j in range(length):
			if i == 0 or j == 0 or i == length - 1 or j == length - 1:
				search_moves(grid, i, j, winning_moves)
	return winning_moves

def print_formatted(winning_moves):
	for move in winning_moves:
		table = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E'}
		print move[0], table[move[1]], move[2]+1, " -> ", table[move[3]], move[4]+1

def solve_quixo():
	grid = generate_grid()
	winning_moves = brute_force(grid)
	print_formatted(winning_moves)

solve_quixo()
