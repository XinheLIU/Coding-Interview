# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        # recursive or iterative
        # if left and right both exist, swap with left-most in the right sub tree
        if not root:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left or not root.right:
                return root.left if not root.right else root.right
            else:
                leftmost = root.right
                while leftmost.left:
                    leftmost = leftmost.left
                root.val = leftmost.val
                root.right = self.deleteNode(root.right, leftmost.val)
        return root