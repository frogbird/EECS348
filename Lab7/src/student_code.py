import common
import math

def detect_slope_intercept(image):
	# PUT YOUR CODE HERE
	# access the image using "image[chanel][y][x]"
	# where 0 <= y < common.constants.WIDTH and 0 <= x < common.constants.HEIGHT 
	# set line.m and line.b
	# to create an auxiliar bidimentional structure 
	# you can use "space=common.init_space(heigh, width)"
	line=common.Line()
	line.m=0
	line.b=0

	#m, b
	voting_space = common.init_space(2000, 2000)
	max_votes = 0
	max_m = 0
	max_b = 0

	for y in range(0, common.constants.HEIGHT):
		for x in range(0, common.constants.WIDTH):
			if image[0][y][x] == 0 and image[1][y][x] == 0 and image[2][y][x] == 0:
				for m in range(-1000, 1000):
					b = -x * m * 0.01 + y
					if b >= -1000 and b < 1000:
						rounded_b = int(b)
						voting_space[m + 1000][rounded_b+1000] += 1
						if voting_space[m + 1000][rounded_b+1000] > max_votes:
							max_m = m * 0.01
							max_b = rounded_b
							max_votes = voting_space[m+1000][rounded_b+1000]

	line.m = max_m
	line.b = max_b

	return line

def detect_normal(image):
	# PUT YOUR CODE HERE
	# access the image using "image[chanel][y][x]"
	# where 0 <= y < common.constants.WIDTH and 0 <= x < common.constants.HEIGHT 
	# set line.theta and line.r
	# to create an auxiliar bidimentional structure 
	# you can use "space=common.init_space(heigh, width)"
	line=common.Line()
	line.r=0
	line.theta=0


	voting_space = common.init_space(1800, 1800)
	max_votes = 0
	max_r = 0
	max_theta = 0

	pi = math.pi
	step_size = pi / 1800

	for y in range(0, common.constants.HEIGHT):
		for x in range(0, common.constants.WIDTH):
			if image[0][y][x] == 0 and image[1][y][x] == 0 and image[2][y][x] == 0:
				for theta in range(0, 1800):
					w = x*math.cos(theta * step_size) + y*math.sin(theta * step_size)
					if w >= -900 and w < 900:
						rounded_w = int(w)
						voting_space[rounded_w + 900][theta] += 1
						if voting_space[rounded_w + 900][theta] > max_votes:
							max_theta = theta * step_size
							max_w = rounded_w
							max_votes = voting_space[rounded_w + 900][theta]

	line.r = max_w
	line.theta = max_theta

	return line

def detect_circles(image):
	# PUT YOUR CODE HERE
	# access the image using "image[chanel][y][x]"
	# where 0 <= y < common.constants.WIDTH and 0 <= x < common.constants.HEIGHT 
	# to create an auxiliar bidimentional structure 
	# you can use "space=common.init_space(heigh, width)"

	new_image = common.init_space(common.constants.HEIGHT, common.constants.WIDTH)

	total2 = 0

	# perform edge detection
	for y in range(1, common.constants.HEIGHT-1):
		for x in range(1, common.constants.WIDTH-1):
			a11 = image[0][y-1][x-1]
			a12 = image[0][y-1][x]
			a13 = image[0][y-1][x+1]
			a21 = image[0][y][x-1]
			a22 = image[0][y][x]
			a23 = image[0][y][x+1]
			a31 = image[0][y+1][x-1]
			a32 = image[0][y+1][x]
			a33 = image[0][y+1][x+1]

			gx = a13 - a11 + 2*a23 - 2*a21 + a33 - a31
			gy = a11 + 2*a12 + a13 - a31 - 2*a32 - a33

			total = abs(gx) + abs(gy)
			new_image[y][x] = total

	voting_space = common.init_space(common.constants.HEIGHT, common.constants.WIDTH)

	max = 0

	for y in range(0, common.constants.HEIGHT):
		for x in range(0, common.constants.WIDTH):
			if new_image[y][x] > 0:
				for i in range(y - 31, y + 31):
					for j in range(x - 31, x + 31):
						if (x - j)**2 + (y - i)**2 >= 895 and (x - j)**2 + (y - i)**2 <= 905:
							if(i >= 0 and i < common.constants.HEIGHT and j >= 0 and j < common.constants.WIDTH):
								voting_space[i][j] += 1
								if voting_space[i][j] > max:
									max = voting_space[i][j]

	# count number of circles
	count = 0
	for i in range(0, common.constants.HEIGHT):
		for j in range(0, common.constants.WIDTH):
			if voting_space[i][j] == max:
				count += 1

	return count
				
