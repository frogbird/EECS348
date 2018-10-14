import common
class variables:
	counter=0

def sudoku_backtracking(sudoku):
	# PUT YOUR CODE HERE
	# access the sudoku using "sudoku[y][x]"
	# y between 0 and 9
	# x between 0 and 9
	# function must return the number of permutations performed
	# the use of variables.counter to keep track of the worlds 
	# explored is optional but recommended 
	variables.counter=0
	# variables.counter+=1000000

	result = bt_recurse(sudoku)

	for i in range(0, 9):
		for j in range(0, 9):
			sudoku[i][j] = result[i][j]
		
	return variables.counter

def bt_recurse(current_board):
	# variables.counter += 1
	# find first open spot
	
	if(checkifComplete(current_board)):
		return current_board

	first_zero = findOpen(current_board)

	if(first_zero != None):
		for z in range(1, 10):
			variables.counter += 1
			if(common.can_yx_be_z(current_board, first_zero[0], first_zero[1], z)):
				new_board = [q[:] for q in current_board]
				new_board[first_zero[0]][first_zero[1]] = z
				result = bt_recurse(new_board)
				if(result != False):
					return result
				else:
					new_board[first_zero[0]][first_zero[1]] = 0

	return False
	

					
def checkifComplete(board):
	for i in range(0, 9):
		for j in range(0, 9):
			if board[i][j] == 0:
				return False
	return True

def findOpen(board):
	for i in range(0,9):
		for j in range(0, 9):
			if board[i][j] == 0:
				return (i, j)

def fc_recurse(current_board):
	# variables.counter += 1
	# find first open spot

	if(checkifComplete(current_board)):
		return current_board

	first_zero = findOpen(current_board)

	if(first_zero != None):
		y = first_zero[0]
		x = first_zero[1]
		for z in range(1, 10):
			if(common.can_yx_be_z(current_board, y, x, z)):
				variables.counter += 1
				new_board = [q[:] for q in current_board]
				new_board[y][x] = z
				result = fc_recurse(new_board)
				if(result != False):
					return result
				else:
					new_board[y][x] = 0

	return False

def sudoku_forwardchecking(sudoku):
	# PUT YOUR CODE HERE
	# access the sudoku using "sudoku[y][x]"
	# y between 0 and 9
	# x between 0 and 9
	# function must return the number of permutations performed
	# the use of variables.counter to keep track of the worlds 
	# explored is optional but recommended 
	variables.counter=0

	result = fc_recurse(sudoku)

	for i in range(0, 9):
		for j in range(0, 9):
			sudoku[i][j] = result[i][j]
	return variables.counter

def build_possible_values(sudoku):
	value_dict = {}
	for j in range(0, 9):
		for i in range(0, 9):
			if(sudoku[i][j] == 0):
				temp = [x for x in range(1, 10) if common.can_yx_be_z(sudoku, i, j, x)]
				value_dict[(i,j)] = temp
	return value_dict


def sudoku_mrv(sudoku):
	# PUT YOUR CODE HERE
	# access the sudoku using "sudoku[y][x]"
	# y between 0 and 9
	# x between 0 and 9
	# function must return the number of permutations performed
	# the use of variables.counter to keep track of the worlds 
	# explored is optional but recommended 
	variables.counter=0
	# variables.counter+=1000000

	result = mrv_recurse(sudoku)

	for i in range(0, 9):
		for j in range(0, 9):
			sudoku[i][j] = result[i][j]
		
	return variables.counter



def mrv_recurse(current_board):
	# variables.counter += 1
	# find first open spot

	if(checkifComplete(current_board)):
		return current_board

	values_remaining = 100
	current_point = None
	dict = build_possible_values(current_board)
	for key in dict:
		current_length = len(dict[key])
		if(current_length < values_remaining):
			values_remaining = current_length
			current_point = key

	if(current_point != None):
		y = current_point[0]
		x = current_point[1]

		for z in range(1, 10):
			if(common.can_yx_be_z(current_board, y, x, z)):
				variables.counter += 1
				new_board = [q[:] for q in current_board]
				new_board[y][x] = z
				result = mrv_recurse(new_board)
				if(result != False):
					return result
				else:
					new_board[y][x] = 0

	return False


