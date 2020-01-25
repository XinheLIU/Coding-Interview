#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def helper(s):
            if len(s) <= 1:
                return s
            else:
                return helper(s[1:]) + [s[0]]
        s[:] = helper(s)
# @lc code=end

