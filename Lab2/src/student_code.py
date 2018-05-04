import common
def astar_search(map):
	found = False
	# PUT YOUR CODE HERE
	# access the map using "map[y][x]"
	# y between 0 and common.constants.MAP_HEIGHT-1
	# x between 0 and common.constants.MAP_WIDTH-1

	root_node = find_starting_location(map)
	queue = [root_node]

	if(root_node == None):
		queue = []

	parent_dictionary = {root_node : None}
	end_point = None

	distance_dictionary = {root_node: 0}

	end = find_ending_location(map)

	while(len(queue) > 0):

		min_cost = 100000
		min_node = None
		min_node_index = None
		# select minimum cost node

		for location in queue:
			temp_cost = find_manhattan_distance(location, end) + distance_dictionary[location]

			if(temp_cost == min_cost):
				if(location[1] == min_node[1]):
					if(location[0] < min_node[0]):
						min_cost = temp_cost
						min_node = location
						min_node_index = queue.index(location)
				elif(location[1] < min_node[1]):
					min_cost = temp_cost
					min_node = location
					min_node_index = queue.index(location)
			elif(temp_cost < min_cost):
				min_cost = temp_cost
				min_node = location
				min_node_index = queue.index(location)

		current_point = queue.pop(min_node_index)

		distance = distance_dictionary[current_point]

		y = current_point[0]
		x = current_point[1]
		
		if(map[y][x] == 3):
			end_point = current_point
			found = True
			break

		else:
			if(map[y][x] != 4):
			
				map[y][x] = 4

				if(x < common.constants.MAP_WIDTH - 1 and map[y][x + 1] != 1 and map[y][x+1] != 4):
					parent_dictionary[(y, x+ 1)] = current_point
					distance_dictionary[(y, x+1)] = distance + 1
					queue.append((y, x+1))

				if(y < common.constants.MAP_HEIGHT - 1 and map[y + 1][x] != 1 and map[y + 1][x] != 4):
					parent_dictionary[(y + 1, x)] = current_point
					distance_dictionary[(y + 1, x)] = distance + 1
					queue.append((y + 1, x))

				if(x > 0 and map[y][x-1] != 1 and map[y][x-1] != 4):
					parent_dictionary[(y, x-1)] = current_point
					distance_dictionary[(y, x-1)] = distance + 1
					queue.append((y, x-1))

				if(y > 0 and map[y-1][x] != 1 and map[y-1][x] != 4):
					parent_dictionary[(y - 1, x)] = current_point
					distance_dictionary[(y - 1, x)] = distance + 1
					queue.append((y - 1, x))
		
	if(end_point != None):
		mark_path(map, end_point, parent_dictionary)

	return found


def find_starting_location(map):
	for y in range(0, common.constants.MAP_HEIGHT):
		for x in range(0, common.constants.MAP_WIDTH):
			if(map[y][x] == 2):
				return (y,x)


def find_ending_location(map):
	for y in range(0, common.constants.MAP_HEIGHT):
		for x in range(0, common.constants.MAP_WIDTH):
			if(map[y][x] == 3):
				return (y,x)
	return (-1, -1)

def find_manhattan_distance(point1, point2):
	if(point2 == (-1, -1)):
		return 0

	else:
		return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


def mark_path(map, end_point, parent_dict):
	current_point = end_point
	while(current_point != None):
		y = current_point[0]
		x = current_point[1]
		map[y][x] = 5
		current_point = parent_dict[current_point]

