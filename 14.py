n, k = [int(x) for x in input().split()]
nums = [int(x) for x in input().split()]
nums.sort()

print(nums[-(k // 2 + 1)])
