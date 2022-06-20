import math


def clockwise_matrix_2(matrix):
    result = []
    x = len(matrix[0])
    y = len(matrix)

    for offset in range(math.ceil(min(x, y) / 2)):
        # top
        for i in range(offset, x - offset):
            result.append(matrix[offset][i])
        # right
        for i in range(offset + 1, y - offset):
            result.append(matrix[i][-offset - 1])
        # bottom
        if y > 1:
            for i in reversed(range(offset + 1, x - offset - 1)):
                result.append(matrix[-offset - 1][i])
        # left
        if x > 1:
            for i in reversed(range(offset + 1, y - offset)):
                result.append(matrix[i][offset])

    return result
