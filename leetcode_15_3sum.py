nums = [int(x) for x in input().split()]
nums.sort()
sums = []

for i in range(len(nums) - 2):
    j = i + 1
    k = len(nums) - 1
    while j != i and j != k:
        cur_sum = nums[i] + nums[j] + nums[k]
        if cur_sum == 0 and [nums[i], nums[j], nums[k]] not in sums:
            sums.append([nums[i], nums[j], nums[k]])
            j += 1
        elif cur_sum > 0:
            k -= 1
        else:
            j += 1

print(sums)
