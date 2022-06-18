from clockwise_matrix import clockwise_matrix_1, clockwise_matrix_2


def test_clockwise():
    result = clockwise_matrix_1([[1, 2], [3, 4]])

    # assert "1 2 4 3" == result
    print(result)

    # result = clockwise_matrix_1([[2, 3, 4, 8],
    #                              [5, 7, 9, 12],
    #                              [1, 0, 6, 10]])

    # assert "2 3 4 8 12 10 6 0 1 5 7 9" == result


test_clockwise()
