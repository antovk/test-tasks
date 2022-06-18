import math
from copy import deepcopy

def clockwise_matrix_1(matrix):
    matrix_copy = deepcopy(matrix)
    result = []
    
    while (matrix_copy):
        result.extend(matrix_copy.pop(0))

        if (matrix_copy and matrix_copy[0]):
            for i in range(len(matrix_copy) - 1):
                result.append(matrix_copy[i].pop(-1))

        if (matrix_copy):
            result.extend(list(reversed(matrix_copy.pop(-1))))

        if (matrix_copy and matrix_copy[-1]):
            for i in list(reversed(range(len(matrix_copy)))):
                result.append(matrix_copy[i].pop(0))
    
    return result


def clockwise_matrix_2(matrix):
    result = []
    x = len(matrix[0])
    y = len(matrix)

    for offset in range(math.ceil(min(x, y) / 2)):

        for i in range(offset, x - offset):
            result.append(matrix[offset][i])

        for i in range(offset + 1, y - offset):
            result.append(matrix[i][-offset - 1])

        if y > 1:
            for i in reversed(range(offset + 1, x - offset - 1)):
                result.append(matrix[-offset - 1][i])

        if x > 1:
            for i in reversed(range(offset + 1, y - offset)):
                result.append(matrix[i][offset])

    return(result)
