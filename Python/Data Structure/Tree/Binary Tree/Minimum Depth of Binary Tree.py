# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
num = float('-inf')
class Solution:
    
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        l, r = self.minDepth(root.left), self.minDepth(root.right)
        return max(l,r) + 1 if not l or not r else min(l,r) + 1