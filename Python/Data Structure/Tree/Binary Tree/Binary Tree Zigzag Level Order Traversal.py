# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def traverse(self, root, level, res):
        if not root:
            return
        # add one more empty layer
        if len(res) == level:
            res.append([])
        if level % 2 == 0:
            res[level].append(root.val)
        else:
            res[level].insert(0, root.val)
        if root.left:
            self.traverse(root.left, level + 1, res)
        if root.right: 
            self.traverse(root.right, level + 1, res)
            
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.res = []
        self.traverse(root, 0, self.res)
        return self.res