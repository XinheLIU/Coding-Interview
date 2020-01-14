#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not len(strs): return ""
        ret = strs[0]
        for i in range(len(strs)):
            j = 0
            while j < len(ret) and j < len(strs[i]):
                if ret[j] != strs[i][j]:
                    break
                j += 1
            ret = ret[0:j]
            if not len(ret): return ret
        return ret
# @lc code=end

