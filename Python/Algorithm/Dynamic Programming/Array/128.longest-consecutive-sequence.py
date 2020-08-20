#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#
# https://leetcode.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Hard (45.17%)
# Likes:    3637
# Dislikes: 187
# Total Accepted:    315.8K
# Total Submissions: 699.2K
# Testcase Example:  '[100,4,200,1,3,2]'
#
# Given an unsorted array of integers, find the length of the longest
# consecutive elements sequence.
# 
# Your algorithm should run in O(n) complexity.
# 
# Example:
# 
# 
# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
# Therefore its length is 4.
# 
# 
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # use a set
        ret, num_set = 0, set(nums)
        for num in nums:
            if num not in num_set:
                continue
            num_set.remove(num)
            pre, nxt = num - 1, num + 1
            while pre in num_set:
                num_set.remove(pre)
                pre -= 1
            while nxt in num_set:
                num_set.remove(nxt)
                nxt += 1
            ret = max(ret, nxt - pre - 1)
        return ret
# @lc code=end

