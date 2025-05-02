n, m = [int(x) for x in input().split()]
nums = [[int(x) for x in input().split()] for _ in range(n)]

max_result = 0
count = 1
for i in range(n):
    if max_result < max(nums[i]):
        max_result = max(nums[i])
        count = 1
    elif max_result == max(nums[i]):
        count += 1
print(count)

# для тестов
# from random import *
# for test in range(1):
#     n = randint(3, 7)
#     m = randint(3, 7)
#     nums = [sorted([randint(1, 15) for _ in range(m)]) for _ in range(n)]
#     print(*nums, sep='\n')
#     print(solution1(n, m, nums))
