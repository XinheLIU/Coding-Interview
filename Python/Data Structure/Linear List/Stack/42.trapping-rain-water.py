#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, heights: List[int]) -> int:
        # decreasing stack
        stack = collections.deque()
        ret = 0
        for i, h in enumerate(heights):
            # decreasing stak
            while stack and h > heights[stack[-1]]:
                t = stack.pop()
                if not stack:
                    continue
                ret += (min(h, heights[stack[-1]]) - heights[t]) * (i - stack[-1] - 1)
            stack.append(i)
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
            # decreasing stack
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
