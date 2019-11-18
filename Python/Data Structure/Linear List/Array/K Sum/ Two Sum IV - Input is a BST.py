# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        s = set()
        return self.helper(root, k, s)
    
    def helper(self, node: TreeNode, k: int, s: set):
        if not node:
            return False
        if k - node.val in s:
            return True
        s.add(node.val)
        return self.helper(node.left, k, s) or self.helper(node.right, k, s)