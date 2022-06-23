import numpy as np
import training_set_generator


def act(x):
    # return 1 / (1 + np.exp(-x))
    return np.maximum(0, x)


# print(training_set_generator.get_set())

training_inputs = np.array([[3, 3, 0, 0],
                            [3, 3, 0, 1],
                            [3, 3, 0, 2],
                            [3, 3, 1, 2],
                            [3, 3, 2, 2],
                            [3, 3, 2, 1],
                            [3, 3, 2, 0],
                            [3, 3, 1, 0],
                            [3, 3, 1, 1]
                            ])

training_outputs = np.array([[0, 1, 2, 3, 4, 5, 6, 7, 8]]).T


synaptic_weights = np.random.random((4, 1)) * 10
print('synaptic_weights' + '--' * 10)
print(synaptic_weights)
for i in range(20000):

    input_layer = training_inputs
    outputs = act(np.dot(input_layer, synaptic_weights))
    # print('outputs' + '--' * 10)
    # print(outputs)
    err = training_outputs - outputs
    # print('error' + '--' * 10)
    # print(err)
    
    adjustments = np.dot(input_layer.T, err * 0.001)
    
    # print('adjustments' + '--' * 10)
    # print(adjustments)

    synaptic_weights += adjustments
    # print(synaptic_weights)
    # break
# else:
    # print('outputs' + '--' * 10)
    # print(outputs)
    # print('error' + '--' * 10)
    # print(err)
    # print('adjustments' + '--' * 10)
    # print(adjustments)

# print(synaptic_weights)

new_inputs = np.array([3, 3, 1, 1])
output = act(np.dot(new_inputs, synaptic_weights))

print('new data:')
print(output)
