# Array division (python)

## Task

![Example](img/array_division_task.png)

---

## [test](https://github.com/antovk/test-tasks/blob/main/array-division/array_division_test.py)

```python
from threading import Timer
import array_division_v1
import array_division_v2
import random
import time


def timer(f):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f.__module__, f(*args, **kwargs), time.time() - start_time)
    return wrapper


arr = random.sample(range(-10_000_000, 10_000_000), 10_000_000)

f1 = timer(array_division_v1.solution)
f2 = timer(array_division_v2.solution)

f1(arr)
f2(arr)
```

## [solution 1](https://github.com/antovk/test-tasks/blob/main/array-division/array_division_v1.py)

```python
def solution(arr):
    max_left = arr[0]
    max_right = max(arr[1:])
    max_diff = abs(max_left - max_right)

    for i in range(1, len(arr) - 1):
        max_left = max(max_left, arr[i])

        if max_right == arr[i]:
            max_right = max(arr[i + 1:])

        max_diff = max(max_diff, abs(max_left - max_right))

    return max_diff

```

## [solution 2](https://github.com/antovk/test-tasks/blob/main/array-division/array_division_v2.py)

```python
import sys


def solution(arr):
    lefts_max = []
    rights_max = []
    max_diff = 0
    max_left = -sys.maxsize - 1
    max_right = -sys.maxsize - 1

    for i in arr[:-1]:
        max_left = max(max_left, i)
        lefts_max.append(max_left)

    for i in arr[:0:-1]:
        max_right = max(max_right, i)
        rights_max.append(max_right)
    rights_max = list(reversed(rights_max))

    # using set to distinct pairs
    dist = set(zip(lefts_max, rights_max))

    for l, r in dist:
        max_diff = max(max_diff, abs(l - r))

    return max_diff

```
