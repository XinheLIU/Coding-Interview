# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        p, stack, ret = root, [None], []
        while p:
            ret.append(p.val)
            if p.right:
                stack.append(p.right)
            if p.left:
                p = p.left
            else:
                p = stack.pop()
        return ret

'''
# recursive
    def preorderTraversal(self, root):
        if not root:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right) 
'''