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
