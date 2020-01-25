#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = collections.Counter()
        l, r = 0, 0
        max_count = 0
        ret = 0
        while r < len(s):
            c1 = s[r]
            count[c1] += 1
            max_count = max(max_count, count[c1])
            while r - l - max_count + 1 > k:
                c2 = s[l]
                count[c2] -= 1
                max_count = max(max_count, count[c2])
                l += 1
            ret = max(ret, r - l + 1)
            r += 1
        return ret
        
# @lc code=end

