import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


training_inputs = np.array([[0, 0, 0],
                            [0, 0, 1],
                            [0, 1, 0],
                            [0, 1, 1],
                            [1, 0, 0],
                            [1, 0, 1],
                            [1, 1, 0],
                            [1, 1, 1]])


training_outputs = np.array([[0, 1, 2, 3, 4, 5, 6, 7]]).T
# print(training_outputs)


np.random.seed(1)

synaptic_weights = 2 * np.random.random((8, 1)) - 1

print(synaptic_weights)

for i in range(20000):

    input_layer = training_inputs
    outputs = sigmoid(np.dot(input_layer, synaptic_weights))

    err = training_outputs - outputs
    adjustments = np.dot(input_layer.T, err * (outputs * (1 - outputs)))

    synaptic_weights += adjustments

# print('result after learning:')
# print(outputs)

new_inputs = np.array([1, 1, 1])
output = sigmoid(np.dot(new_inputs, synaptic_weights))

print('new data:')
print(output)
