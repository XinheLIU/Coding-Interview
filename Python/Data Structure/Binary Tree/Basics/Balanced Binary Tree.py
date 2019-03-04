# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # returns -1 or depth
    def helper(self, root):
        if not root:
            return 0
        l, r = self.helper(root.left), self.helper(root.right)
        if l == -1 or r == -1 or (abs(l-r) > 1):
            return -1
        return max(l,r) + 1
        
        
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root) != -1 