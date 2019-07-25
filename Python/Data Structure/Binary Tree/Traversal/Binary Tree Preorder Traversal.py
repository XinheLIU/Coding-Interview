rs# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        node, stack, ret = root, [None], []
        while node:
            ret.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                node = node.left
            else:
                node = stack.pop()
        return ret

'''
# recursive
    def preorderTraversal(self, root):
        if not root:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right) 
'''