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
