import math

nums = [1, 2, 5, 9]
threshold = 6


def f(arr, divisor):
    return sum([math.ceil(x / divisor) for x in arr])


l, r = 0, 10 ** 10
while l + 1 != r:
    c = (l + r) // 2
    if f(nums, c) > threshold:
        l = c
    else:
        r = c

print(r)
