# n, m = [int(x) for x in input().split()]
# nums = [[int(x) for x in input().split()] for _ in range(n)]

def solution1(n, m, nums):
    max_result = 0
    count = 1
    for i in range(n):
        if max_result < max(nums[i]):
            max_result = max(nums[i])
            count = 1
        elif max_result == max(nums[i]):
            count += 1
    return count, max_result

def solution2(n, m, nums):
    max_result = 0
    count = 1
    for i in range(n):
        flag = False
        for j in range(m):
            if max_result < nums[i][j]:
                max_result = nums[i][j]
                count = 1
                flag = False
            elif max_result == nums[i][j]:
                flag = True
        if flag:
            count += 1

    return count

from random import *
for test in range(1000):
    n = randint(3, 7)
    m = randint(3, 7)
    nums = [[randint(1, 15) for _ in range(m)] for _ in range(n)]
    assert solution1(n, m, nums) == solution2(n, m, nums), f'{n, m, nums}, {solution1(n, m, nums)}, {solution2(n, m, nums)}'

