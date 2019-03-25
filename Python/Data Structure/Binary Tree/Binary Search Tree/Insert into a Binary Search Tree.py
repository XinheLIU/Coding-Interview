# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoBST(self, root, key):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return TreeNode(key)
        elif key < root.val:
            root.left = self.insertIntoBST(root.left, key) if root.left else TreeNode(key)
        elif key > root.val:
            root.right = self.insertIntoBST(root.right, key) if root.right else TreeNode(key)
        # equal, do nothing
        return root