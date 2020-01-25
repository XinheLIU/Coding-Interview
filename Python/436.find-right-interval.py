#
# @lc app=leetcode id=436 lang=python3
#
# [436] Find Right Interval
#

# @lc code=start
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        # start, index
        ns = sorted([(d[0], i) for i, d in enumerate(intervals)])
        res = []
        for d in intervals:
            index = d[1]
            if index > ns[-1][0]: # right of the larget
                res.append(-1)
            elif index <= ns[0][0]: # left of the smallest
                res.append(ns[0][1])
            else:
                l, r = 0, len(ns)-1 # search in sorted start
                while l + 1 < r:
                    m = (r + l) >> 1
                    if ns[m][0] >= index: # index in the left of the mid (left most)
                        r = m
                    else:
                        l = m
                res.append(ns[r][1])
        return res
# @lc code=end

