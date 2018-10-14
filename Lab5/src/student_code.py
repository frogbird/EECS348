import common
def drone_flight_planner (map,policies, values, delivery_fee, battery_drop_cost, dronerepair_cost, discount_per_cycle):
	# PUT YOUR CODE HERE
	# access the map using "map[y][x]"
	# access the policies using "policies[y][x]"
	# access the values using "values[y][x]"
	# y between 0 and 5
	# x between 0 and 5
	# function must return the value of the cell corresponding to the starting position of the drone

	gamma = 1-discount_per_cycle
	constants_list = [common.constants.SOFF, common.constants.WOFF, common.constants.NOFF, common.constants.EOFF,
			common.constants.SON, common.constants.WON, common.constants.NON, common.constants.EON]

	for y in range(0, 6):
		for x in range(0, 6):
			if map[y][x] == common.constants.PIZZA:
				starting_spot = (y,x)
			elif map[y][x] == common.constants.RIVAL:
				values[y][x] = -dronerepair_cost
				optimal_policy = common.constants.EXIT
			elif map[y][x] == common.constants.CUSTOMER:
				values[y][x] = delivery_fee
				optimal_policy = common.constants.EXIT


	k = 0
	difference = 10000
	while(difference > 0.10):
		k += 1
		difference = 0
		for i in range(0, 6):
			for j in range(0, 6):
				if(map[i][j] == common.constants.PIZZA or map[i][j] == common.constants.EMPTY):
					current_state = (i, j)
					current_reward = -battery_drop_cost

					if(j==0):
						west_state = current_state
					else:
						west_state = (i, j - 1)
				
					if(i==0):
						north_state = current_state
					else:
						north_state = (i - 1 , j)
					if(i==5):
						south_state = current_state
					else:
						south_state = (i + 1, j)
					if(j == 5):
						east_state = current_state
					else:
						east_state = (i, j + 1)

					going_south_normal = current_reward + gamma*values[south_state[0]][south_state[1]]
					going_south_special = current_reward*2 + gamma*values[south_state[0]][south_state[1]]
					going_west_normal = current_reward + gamma*values[west_state[0]][west_state[1]]
					going_west_special = current_reward*2 + gamma*values[west_state[0]][west_state[1]]

					going_north_normal = current_reward + gamma*values[north_state[0]][north_state[1]]
					going_north_special = current_reward*2 + gamma*values[north_state[0]][north_state[1]]
					going_east_normal = current_reward + gamma*values[east_state[0]][east_state[1]]
					going_east_special = current_reward*2 + gamma*values[east_state[0]][east_state[1]]
								
					south_action_normal = 0.7*going_south_normal + 0.15*going_east_normal + 0.15*going_west_normal
					south_action_special = 0.8*going_south_special + 0.1*going_east_special + 0.1*going_west_special

					west_action_normal = 0.7*going_west_normal + 0.15*going_south_normal + 0.15*going_north_normal
					west_action_special = 0.8*going_west_special + 0.1*going_south_special + 0.1*going_north_special

					north_action_normal = 0.7*going_north_normal + 0.15*going_west_normal + 0.15*going_east_normal
					north_action_special = 0.8*going_north_special + 0.1*going_west_special + 0.1*going_east_special

					east_action_normal = 0.7*going_east_normal + 0.15*going_north_normal + 0.15*going_south_normal
					east_action_special = 0.8*going_east_special + 0.1*going_north_special + 0.1*going_south_special

					value_list = [south_action_normal, west_action_normal, north_action_normal, east_action_normal,
					south_action_special, west_action_special, north_action_special, east_action_special]

					best_value = max(value_list)
					policies[i][j] = constants_list[value_list.index(best_value)]

					#check convergence
					difference += abs(best_value - values[i][j])

					values[i][j] = best_value
	
	return values[starting_spot[0]][starting_spot[1]]			 
			
	
