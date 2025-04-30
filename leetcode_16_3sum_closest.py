nums = [-4, 2, 2, 3, 3, 3]
target = 0
nums.sort()
closest_sum = 0
diff = float('inf')

for i in range(len(nums) - 2):
    j, k = i + 1, len(nums) - 1
    while j < k:
        cur_sum = nums[i] + nums[j] + nums[k]
        if abs(cur_sum - target) < diff:
            diff = abs(cur_sum - target)
            closest_sum = cur_sum
        if cur_sum > target:
            k -= 1
        else:
            j += 1

print(closest_sum)
