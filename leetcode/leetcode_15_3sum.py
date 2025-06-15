nums = [0, 0, 0]

nums.sort()
sums = []

for i in range(len(nums) - 2):
    k, j = i + 1, len(nums) - 1
    while k < j:
        cur_sum = nums[i] + nums[k] + nums[j]
        if cur_sum == 0 and [nums[i], nums[k], nums[j]] not in sums:
            sums.append([nums[i], nums[k], nums[j]])
            k += 1
        elif cur_sum > 0:
            j -= 1
        else:
            k += 1

print(sums)
