nums = [2, 2, 2, 2, 2]
target = 8
nums.sort()
quadruplets = []
n = len(nums)
for i in range(n):
    for j in range(i + 1, n):
        k, m = j + 1, n - 1
        while k < m:
            cur_sum = nums[i] + nums[j] + nums[k] + nums[m]
            if cur_sum > target:
                m -= 1
            elif cur_sum < target:
                k += 1
            else:
                if [nums[i], nums[j], nums[k], nums[m]] not in quadruplets:
                    quadruplets.append([nums[i], nums[j], nums[k], nums[m]])
                k += 1
print(quadruplets)
