import math


def clockwise_matrix_2(matrix):
    result = []
    x = len(matrix[0])
    y = len(matrix)
    offset_range = range(math.ceil(min(x, y) / 2))

    for offset in offset_range:

        # top
        for i in range(offset, x - offset):
            result.append(matrix[offset][i])

        # right
        for i in range(offset + 1, y - offset):
            result.append(matrix[i][-offset - 1])

        # bottom
        if (y - 2 * offset - 1 != 0):
            for i in reversed(range(offset, x - offset - 1)):
                result.append(matrix[-offset - 1][i])

        # left
        if (x - 2 * offset - 1 != 0):
            for i in reversed(range(offset + 1, y - offset - 1)):
                result.append(matrix[i][offset])

    return result


# print(clockwise_matrix_2(MATRIX_7))
