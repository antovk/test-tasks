
from tracemalloc import start
import numpy as np
import clockwise_matrix_2

for i in range(1):
    matrix = np.random.randint(100,
                            size=(np.random.randint(1, 5),
                                  np.random.randint(1, 5))
                            ).tolist()

    matrix_1d = []
    for x in matrix:
        matrix_1d.extend(x)

    cw_2 = clockwise_matrix_2.clockwise_matrix_2(matrix)

    print(matrix_1d, len(matrix[0]), len(matrix))
    print(cw_2)

    