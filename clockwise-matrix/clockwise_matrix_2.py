import math


def clockwise_matrix_2(matrix):
    result = []
    columns = len(matrix[0])
    rows = len(matrix)
    offset_range = range(math.ceil(min(columns, rows) / 2))

    for offset in offset_range:
        # top
        for i in range(offset, columns - offset):
            result.append(matrix[offset][i])
        # right
        for i in range(offset + 1, rows - offset):
            result.append(matrix[i][-offset - 1])
        # bottom
        if (rows - 2 * offset - 1 != 0):
            for i in reversed(range(offset, columns - offset - 1)):
                result.append(matrix[-offset - 1][i])
        # left
        if (columns - 2 * offset - 1 != 0):
            for i in reversed(range(offset + 1, rows - offset - 1)):
                result.append(matrix[i][offset])

    return result
