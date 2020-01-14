#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ret = 0
        l, r = 0, 0
        window = collections.defaultdict(int)
        while r < len(s):
            c1 = s[r]
            window[c1] += 1
            r += 1
            while window[c1] > 1: # repeating, move left
                c2 = s[l]
                window[c2] -= 1
                l += 1
            ret = max(ret, r - l)
        return ret
# @lc code=end

