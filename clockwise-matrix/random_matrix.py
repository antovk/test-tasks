
import numpy as np
import clockwise_matrix_2
import clockwise_matrix_1

for i in range(10):
    m = np.random.randint(100,
                          size=(np.random.randint(1, 5),
                                np.random.randint(1, 5))
                          ).tolist()

    l = []
    for x in m:
        l.extend(x)

    cw_1 = clockwise_matrix_1.clockwise_matrix_1(m)
    cw_2 = clockwise_matrix_2.clockwise_matrix_2(m)

    print(l)
    print(cw_1)
    print(cw_2)

    assert len(l) == len(cw_1) == len(cw_2) and cw_1 == cw_2

else:
    print('OK')
