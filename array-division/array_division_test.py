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


arr = random.sample(range(-1_000_000, 1_000_000), 1_000_000)

f1 = timer(array_division_v1.solution)
f2 = timer(array_division_v2.solution)

f1(arr)
f2(arr)