# Make a prediction with weights
def perceptron_predict(inputs, weights):
	activation = weights[0]
	for i in range(len(inputs)-1):
		activation += weights[i + 1] * inputs[i]
	return 1.0 if activation  >= 0.0 else 0.0

# Estimate Perceptron weights using stochastic gradient descent
def train_weights(train, learning_rate, n_epoch):
	weights = [0.0 for i in range(len(train[0]))]
	for epoch in range(n_epoch):
		sum_error = 0.0
		for inputs in train:
			prediction = perceptron_predict(inputs, weights)
			error = inputs[-1] - prediction
			sum_error += error**2
			weights[0] = weights[0] + learning_rate * error
			for i in range(len(inputs)-1):
				weights[i + 1] = weights[i + 1] + learning_rate * error * inputs[i]
		print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, learning_rate, sum_error))
	return weights

train = [[1.5,2.5,0],[2.5,3.5,0],[1.0,11.0,1],[2.3,2.3,1],[3.6,3.6,1],[4.2,2.4,0],[2.4,5.4,0],[5.1,5.1,1],[4.3,1.3,0],[4.8,4.8,1]]

learning_rate = 0.1
epochs = 10
weights = train_weights(train, learning_rate, epochs)
print(weights)
