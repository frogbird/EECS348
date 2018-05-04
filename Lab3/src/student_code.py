import common

def minmax_tictactoe(board, turn):
	if(turn == common.constants.X):
		outcome = max_value(board, turn)
	elif(turn == common.constants.O):
		outcome = min_value(board, turn)

	if(outcome == 1):
		return common.constants.X
	elif(outcome == -1):
		return common.constants.O
	else:
		return common.constants.NONE

	return common.constants.NONE

def abprun_tictactoe(board, turn):
	if(turn == common.constants.X):
		outcome = abmax_value(board, turn, -1, 1)
	elif(turn == common.constants.O):
		outcome = abmin_value(board, turn, -1, 1)

	if(outcome == 1):
		return common.constants.X
	elif(outcome == -1):
		return common.constants.O
	else:
		return common.constants.NONE

	return common.constants.NONE


def max_value(board, turn):
	v = -1000

	if(turn == common.constants.X):
		next_turn = common.constants.O
	else:
		next_turn = common.constants.X
	complete = True
	board_state = common.game_status(board)

	if(board_state == common.constants.X):
		v = 1
	elif(board_state == common.constants.O):
		v = -1

	else:
		# check if board is complete
		for i in range(3):
			for j in range(3):
				if(common.get_cell(board, i, j) == common.constants.NONE):
					complete = False
					successor_board = board[:]
					common.set_cell(successor_board, i, j, turn)
					v = max(v, min_value(successor_board, next_turn))
		if(complete):
			v = 0
	return v



def min_value(board, turn):
	v = 1000

	if(turn == common.constants.X):
		next_turn = common.constants.O
	else:
		next_turn = common.constants.X
	complete = True
	board_state = common.game_status(board)

	if(board_state == common.constants.X):
		v = 1
	elif(board_state == common.constants.O):
		v = -1
	else:
		for i in range(3):
			for j in range(3):
				if(common.get_cell(board, i, j) == common.constants.NONE):
					complete = False
					successor_board = board[:]
					common.set_cell(successor_board, i, j, turn)
					v = min(v, max_value(successor_board, next_turn))
		if(complete):
			v = 0
	return v
				

def abmax_value(board, turn, a, b):

	v = -1000

	if(turn == common.constants.X):
		next_turn = common.constants.O
	else:
		next_turn = common.constants.X
	complete = True
	
	board_state = common.game_status(board)
	if(board_state == common.constants.X):
		v = 1
	elif(board_state == common.constants.O):
		v = -1
	else:
		for i in range(3):
			for j in range(3):
				if(common.get_cell(board, i, j) == common.constants.NONE):
					complete = False
					successor_board = board[:]
					common.set_cell(successor_board, i, j, turn)
					v = max(v, abmin_value(successor_board, next_turn, a, b))
					if v >= b:
						return v
					a = max(a, v)

		if(complete):
			v = 0
	return v

def abmin_value(board, turn, a, b):
	v = 1000

	if(turn == common.constants.X):
		next_turn = common.constants.O
	else:
		next_turn = common.constants.X
	complete = True

	board_state = common.game_status(board)
	if(board_state == common.constants.X):
		v = 1
	elif(board_state == common.constants.O):
		v = -1
	else:
		for i in range(3):
			for j in range(3):
				if(common.get_cell(board, i, j) == common.constants.NONE):
					complete = False
					successor_board = board[:]
					common.set_cell(successor_board, i, j, turn)
					v = min(v, abmax_value(successor_board, next_turn, a, b))
					if v <= a:
						return v
					b = min(b, v)

		if(complete):
			v = 0
	return v
