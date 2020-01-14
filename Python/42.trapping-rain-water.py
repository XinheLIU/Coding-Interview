#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, heights: List[int]) -> int:
        if not heights:
            return 0
            
        max_l = []
        curt_max = -sys.maxsize
        for height in heights:
            curt_max = max(curt_max, height)
            max_l.append(curt_max)
            
        max_r = []
        curt_max = -sys.maxsize
        for height in reversed(heights):
            curt_max = max(curt_max, height)
            max_r.append(curt_max)
            
        max_r = max_r[::-1]
            
        ret = 0
        n = len(heights)
        for i in range(n):
            ret += (min(max_l[i], max_r[i]) - heights[i])
        return ret

# @lc code=end
'''
class Solution:
    # decreasing stack
    def trap(self, height: List[int]) -> int:
        stack = collections.deque()
        i = 0
        ret = 0
        n = len(height)
        while i < n:
            if not stack or height[stack[-1]] >= height[i]:
                stack.append(i)
                i += 1
            else:
                t = stack.pop()
                if not stack:
                    continue
                ret += (min(height[i], height[stack[-1]]) - height[t]) * (i - stack[-1] - 1)
        return ret
'''
class Solution:
    # brute force
    def trap(self, height: List[int]) -> int:
        ret = 0
        for i, h in enumerate(height):
            if 0 < i < len(height) - 1:
                max_l, max_r = max(height[:i]), max(height[i+1:])
                ret += max(min(max_l, max_r) - h, 0)
        return ret
'''