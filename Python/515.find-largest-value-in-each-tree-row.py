#
# @lc app=leetcode id=515 lang=python3
#
# [515] Find Largest Value in Each Tree Row
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        hashMap = {}
        def dfs(root, depth, hashMap):
            if not root:
                return
            else:
                if depth not in hashMap:
                    hashMap[depth] = root.val
                else:
                    hashMap[depth] = max(root.val, hashMap[depth])
            dfs(root.left, depth + 1, hashMap)
            dfs(root.right, depth + 1, hashMap)
        dfs(root, 1, hashMap)
        return [hashMap[i] for i in hashMap]

        
# @lc code=end

