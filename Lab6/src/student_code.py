import common

def part_one_classifier(data_train,data_test):
	# PUT YOUR CODE HERE
	# Access the training data using "data_train[i][j]"
	# Training data contains 3 cols per row: X in 
	# index 0, Y in index 1 and Class in index 2
	# Access the test data using "data_test[i][j]"
	# Test data contains 2 cols per row: X in 
	# index 0 and Y in index 1, and a blank space in index 2 
	# to be filled with class
	# The class value could be a 0 or a 1

	w = [0, 0, 0]
	classifier_error = 1000

	while(classifier_error > 1):
	
		for i in range(0, common.constants.TRAINING_SIZE):
			dot_product = w[0] * data_train[i][0] + w[1] * data_train[i][1] + w[2]
			if dot_product >= 0:
				classifier = 1
			else:
				classifier = 0

			if classifier != data_train[i][2]:
				if data_train[i][2] == 1:
					w[0] = w[0] + data_train[i][0]
					w[1] = w[1] + data_train[i][1]
					w[2] = w[2] + 1

				else:
					w[0] = w[0] - data_train[i][0]
					w[1] = w[1] - data_train[i][1]
					w[2] = w[2] - 1


		sum = 0
		for i in range(0, common.constants.TRAINING_SIZE):
			dot_product = w[0] * data_train[i][0] + w[1]*data_train[i][1] + w[2]
			if dot_product >= 0:
				classifier = 1
			else:
				classifier = 0
			if classifier != data_train[i][2]:
				sum += 1

		classifier_error = sum

	for j in range(0, common.constants.TEST_SIZE):
		dot_product = w[0] * data_test[j][0] + w[1] * data_test[j][1] + w[2]
		if dot_product >= 0:
			classifier = 1
		else:
			classifier = 0
		
		data_test[j][2] = classifier
	return

def part_two_classifier(data_train,data_test):
	# PUT YOUR CODE HERE
	# Access the training data using "data_train[i][j]"
	# Training data contains 3 cols per row: X in 
	# index 0, Y in index 1 and Class in index 2
	# Access the test data using "data_test[i][j]"
	# Test data contains 2 cols per row: X in 
	# index 0 and Y in index 1, and a blank space in index 2 
	# to be filled with class
	# The class value could be a 0 or a 8

	w = [[0, 0, 0]for x in range(0, 9)]

	classifier_error = 1000
	while(classifier_error > 50):
		for i in range(0, common.constants.TRAINING_SIZE):
			values = [perform_dot_product(x, data_train[i]) for x in w]
			classifier = values.index(max(values))
			if classifier != data_train[i][2]:
				correct = int(data_train[i][2])

				w[classifier][0] -= data_train[i][0]
				w[classifier][1] -= data_train[i][1]
				w[classifier][2] -= 1
			
				w[correct][0] += data_train[i][0]
				w[correct][1] += data_train[i][1]
				w[correct][2] += 1
		
		sum = 0
		for i in range(0, common.constants.TRAINING_SIZE):
			values = [perform_dot_product(x, data_train[i]) for x in w]
			classifier = values.index(max(values))
			if classifier != data_train[i][2]:
				sum += 1
		classifier_error = sum

	for j in range(0, common.constants.TEST_SIZE):
		values = [perform_dot_product(x, data_test[j]) for x in w]
		classifier = values.index(max(values))
		
		data_test[j][2] = classifier

	return

def perform_dot_product(w, feature):
	return w[0]*feature[0] + w[1]*feature[1] + w[2]
