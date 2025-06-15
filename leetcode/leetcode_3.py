class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        i = 0
        last_seen = {}
        mlen = 0
        for j, char in enumerate(s):
            if char in last_seen and last_seen[char] >= i:
                i = last_seen[char] + 1
            last_seen[char] = j
            mlen = max(mlen, j - i + 1)
        return mlen
