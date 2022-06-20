from copy import deepcopy


def clockwise_matrix_1(matrix):
    matrix_copy = deepcopy(matrix)
    result = []

    while (matrix_copy):
        # top
        result.extend(matrix_copy.pop(0))
        # right
        if (matrix_copy and matrix_copy[0]):
            for i in range(len(matrix_copy) - 1):
                result.append(matrix_copy[i].pop(-1))
        # bottom
        if (matrix_copy):
            result.extend(list(reversed(matrix_copy.pop(-1))))
        # left
        if (matrix_copy and matrix_copy[-1]):
            for i in list(reversed(range(len(matrix_copy)))):
                result.append(matrix_copy[i].pop(0))

    return result
