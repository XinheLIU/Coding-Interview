#
# @lc app=leetcode id=832 lang=python3
#
# [832] Flipping an Image
#
# https://leetcode.com/problems/flipping-an-image/description/
#
# algorithms
# Easy (76.30%)
# Likes:    930
# Dislikes: 150
# Total Accepted:    178.3K
# Total Submissions: 233.6K
# Testcase Example:  '[[1,1,0],[1,0,1],[0,0,0]]'
#
# Given a binary matrix A, we want to flip the image horizontally, then invert
# it, and return the resulting image.
# 
# To flip an image horizontally means that each row of the image is reversed.
# For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].
# 
# To invert an image means that each 0 is replaced by 1, and each 1 is replaced
# by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].
# 
# Example 1:
# 
# 
# Input: [[1,1,0],[1,0,1],[0,0,0]]
# Output: [[1,0,0],[0,1,0],[1,1,1]]
# Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
# Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
# 
# 
# Example 2:
# 
# 
# Input: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
# Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
# Explanation: First reverse each row:
# [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
# Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
# 
# 
# Notes:
# 
# 
# 1 <= A.length = A[0].length <= 20
# 0 <= A[i][j] <= 1
# 
# 
#

# @lc code=start
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for row in A:
            for i in range((len(row) + 1) // 2):
                #In Python, the shortcut row[~i] = row[-i-1] = row[len(row) - 1 - i]
                row[i], row[~i] = row[~i] ^ 1, row[i] ^ 1
        return A
        
# @lc code=end

