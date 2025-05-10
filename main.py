nums = [2, 3, 1, 2, 4, 3]
target = 7
mlen = float('inf')
l = 0
cur_sum = 0
for r in range(len(nums)):
    cur_sum += nums[r]
    while cur_sum >= target:
        mlen = min(mlen, r - l + 1)
        cur_sum -= nums[l]
        l += 1

print(mlen)
0 if cur_sum == 'inf' else print(1)