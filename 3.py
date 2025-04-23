# решение 1
# N = int(input())
# nums = [int(x) for x in input().split()]
# summ = 0
# for x in nums:
#     for y in nums:
#         summ += int(str(x) + str(y))
#
# print(summ)

# решение 2
# n = int(input())
# nums = [int(x) for x in input().split()]
#
# total = 0
# a = 0
# for x in nums:
#     a += int(str(x) + str(nums[0]))
#
# b = (a - int(str(nums[0]) * 2) * n) // 10  # кол-во десяток
# for x in nums:
#     total += (int(str(nums[0]) + str(x)) * n) + b * 10
# print(total)