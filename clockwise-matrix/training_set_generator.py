
import numpy as np
import math


def generate_matrix(min_val=0, max_val=1, max_width=10, max_height=10):
    matrix = np.random.randint(min_val, max_val,
                               size=(np.random.randint(1, max_height),
                                     np.random.randint(1, max_width))
                               ).tolist()

    # matrix_1d = []
    # for x in matrix:
    #     matrix_1d.extend(x)

    return matrix


def generate_set(matrix):
    result = []
    columns = len(matrix[0])
    rows = len(matrix)
    offset_range = range(math.ceil(min(columns, rows) / 2))
    dest_pos = 0

    for offset in offset_range:
        # top
        for i in range(offset, columns - offset):
            result.append([rows, columns, offset, i, dest_pos])
            dest_pos += 1
        # right
        for i in range(offset + 1, rows - offset):
            result.append([rows, columns, i, columns - offset - 1, dest_pos])
            dest_pos += 1
        # bottom
        if (rows - 2 * offset - 1 != 0):
            for i in reversed(range(offset, columns - offset - 1)):
                result.append([rows, columns, rows - offset - 1, i, dest_pos])
                dest_pos += 1
        # left
        if (columns - 2 * offset - 1 != 0):
            for i in reversed(range(offset + 1, rows - offset - 1)):
                result.append([rows, columns, i, offset, dest_pos])
                dest_pos += 1

    return result


def get_set():
    return(generate_set(generate_matrix()))