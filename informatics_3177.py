nums = [int(x) for x in input().split()]
k = int(input())

x = 0
for i in range(k % len(nums)):
    x = nums[-1]
    nums[-1] = 0
    for j in range(len(nums) - 1, 0, -1):
        nums[j], nums[j - 1] = nums[j - 1], nums[j]
    nums[0] = x

print(*nums)
