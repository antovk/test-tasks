from clockwise_matrix_1 import clockwise_matrix_1
from clockwise_matrix_2 import clockwise_matrix_2
from matrix_examples import *


def test_clockwise(matrix, result):
    result_1 = clockwise_matrix_1(matrix)
    result_2 = clockwise_matrix_2(matrix)

    assert result_1 == result_2 == result


matrices = [MATRIX_1, MATRIX_2, MATRIX_3, MATRIX_4,
            MATRIX_5, MATRIX_6, MATRIX_7, MATRIX_8, MATRIX_9]

results = [RESULT_1, RESULT_2, RESULT_3, RESULT_4,
           RESULT_5, RESULT_6, RESULT_7, RESULT_8, RESULT_9]

for m, r in zip(matrices, results):
    test_clockwise(m, r)
else:
    print('All OK')
