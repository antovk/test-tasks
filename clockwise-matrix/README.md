# Clockwise Matrics (python)

## Task

_Write a function that, given a matrix of integers, builds a list with the entries of that matrix appended in clockwise order._

```python
input = [[ 1,  2,  3, 4],
         [10, 11, 12, 5],
         [ 9,  8,  7, 6]]

clockwiseMatrix(input)
>>[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
```

---

### Solution 1

First solution I`v desided to make as simple as possible.\
In this solution makes a deepcopy of the input argument and "cut" the side of the new matrix after each "rotation".

![Untitled](img/cw1.png)

- [solution_1](https://github.com/antovk/test-tasks/blob/main/clockwise-matrix/clockwise_matrix_1.py)

```python
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

```

---

### Solution 2

In the second solution I consider source matrix as multiple matrices nested one each other with own offsets.\
At each cycle iteration get the values from the four sides of the matrix, after which offset is increased by 1.\
Initial position of each offset is top left corner (1, 17, 25)

- **rows** - height of source matrix (number of rows)
- **columns** - width of source matrix (number of columns)
- **offset** - matrix offset (outer matrix offset = 0, next offset = 1 etc.)

  ![Untitled](img/cw2.png)

- [solution_2](https://github.com/antovk/test-tasks/blob/main/clockwise-matrix/clockwise_matrix_2.py)

```python
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

```
