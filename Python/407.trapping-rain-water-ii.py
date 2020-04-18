#
# @lc app=leetcode id=407 lang=python3
#
# [407] Trapping Rain Water II
#

# @lc code=start
import heapq
class Solution:
    def trapRainWater(self, heights: List[List[int]]) -> int:
        if not heights: return 0
        self.initialize(heights)
        water = 0

        while self.borders:
            height, x, y = heapq.heappop(self.borders)
            for x_, y_ in self.adjacent(x, y):
                water += max(0, height - heights[x_][y_])
                self.add(x_, y_, max(height, heights[x_][y_]))
        return water
    
    def initialize(self, heights):
        self.n = len(heights)
        self.m = len(heights[0])
        self.visited = set()
        self.borders = []

        for index in range(self.n):
            self.add(index, 0, heights[index][0])
            self.add(index, self.m - 1, heights[index][self.m - 1])
            
        for index in range(self.m):
            self.add(0, index, heights[0][index])
            self.add(self.n - 1, index, heights[self.n - 1][index])
    
    def add(self, x, y, height):
        heapq.heappush(self.borders, (height, x, y))
        self.visited.add((x, y))
    
    def adjacent(self, x, y):
        adj = []
        for delta_x, delta_y in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            x_ = x + delta_x
            y_ = y + delta_y
            if 0 <= x_ < self.n and 0 <= y_ < self.m and (x_, y_) not in self.visited:
                adj.append((x_, y_))
        return adj
# @lc code=end

