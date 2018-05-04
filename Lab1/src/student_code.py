import common
def df_search(map):
	found = False
	# PUT YOUR CODE HERE
	# access the map using "map[y][x]"
	# y between 0 and common.constants.MAP_HEIGHT-1
	# x between 0 and common.constants.MAP_WIDTH-1

	root_node = find_starting_location(map)

	stack = [root_node]

	parent_dictionary = {root_node : None}

	end_point = None

	while(len(stack) > 0):

		current_point = stack.pop()

		y = current_point[0]
		x = current_point[1]

		if(map[y][x] == 3):
			end_point = current_point
			found = True
			break

		else:
			# if not visited
			if(map[y][x] != 4):

				# mark visited
				map[y][x] = 4

				if(y > 0 and map[y-1][x] != 1 and map[y-1][x] != 4):
					parent_dictionary[(y-1,x)] = current_point
					stack.append((y-1,x))

				if(x > 0 and map[y][x-1] != 1 and map[y][x-1] != 4):
					parent_dictionary[(y, x-1)] = current_point
					stack.append((y, x-1))

				if(y < common.constants.MAP_HEIGHT-1 and map[y+1][x] != 1 and map[y+1][x] != 4):
					parent_dictionary[(y + 1, x)] = current_point
					stack.append((y+1, x))

				if(x < common.constants.MAP_WIDTH-1 and map[y][x+1] != 1 and map[y][x+1] != 4):
					parent_dictionary[(y, x+1)] = current_point
					stack.append((y, x+1))

	if(end_point != None):
		mark_path(map, end_point, parent_dictionary)

	return found



def bf_search(map):
	found = False
	# PUT YOUR CODE HERE
	# access the map using "map[y][x]"
	# y between 0 and common.constants.MAP_HEIGHT-1
	# x between 0 and common.constants.MAP_WIDTH-1
	
	root_node = find_starting_location(map)

	queue = [root_node]

	parent_dictionary = {root_node : None}

	end_point = None

	while(len(queue) > 0):

		current_point = queue.pop(0)

		y = current_point[0]
		x = current_point[1]

		if(map[y][x] == 3):
			end_point = current_point
			found = True
			break

		else:
			# if not visited
			if(map[y][x] != 4):

				# mark visited
				map[y][x] = 4

				if(x < common.constants.MAP_WIDTH-1 and map[y][x + 1] != 1 and  map[y][x+1] != 4):
					parent_dictionary[(y, x + 1)] = current_point	
					queue.append((y, x + 1))
	
				if(y < common.constants.MAP_HEIGHT-1 and map[y + 1][x] != 1 and map[y+1][x] != 4):
					parent_dictionary[(y + 1, x)] = current_point
					queue.append((y + 1, x))

				if(x > 0 and map[y][x - 1] != 1 and map[y][x-1] != 4):
					parent_dictionary[(y, x - 1)] = current_point
					queue.append((y, x - 1))

				if(y > 0 and map[y - 1][x] != 1 and map[y-1][x] != 4):
					parent_dictionary[(y - 1, x)] = current_point
					queue.append((y - 1, x))


	if(end_point != None):
		mark_path(map, end_point, parent_dictionary)

	return found

def find_starting_location(map):
	for y in range(0, common.constants.MAP_HEIGHT-1):
		for x in range(0, common.constants.MAP_WIDTH-1):
			if(map[y][x] == 2):
				return (y,x)



def mark_path(map, end_point, parent_dict):

	current_point = end_point
	while(current_point != None):
		y = current_point[0]
		x = current_point[1]
		map[y][x] = 5
		current_point = parent_dict[current_point]

