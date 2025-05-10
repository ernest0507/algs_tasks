class Solution(object):
    def minSubArrayLen(self, target, nums):
        l = 0
        cur_sum = 0
        mlen = float('inf')
        for r in range(len(nums)):
            cur_sum += nums[r]
            while cur_sum >= target:
                mlen = min(mlen, r - l + 1)
                cur_sum -= nums[l]
                l += 1
        return 0 if mlen == float('inf') else mlen