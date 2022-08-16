from threading import Timer
import array_division_v1
import random
import time


def timer(f):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f.__module__, f(*args, **kwargs), time.time() - start_time)
    return wrapper


arr = random.sample(range(-10_000_000, 10_000_000), 10_000_000)

f1 = timer(array_division_v1.solution)

f1(arr)
