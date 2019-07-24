# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ret, node, stack = [], root, []
        while node or len(stack):
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            ret.append(node.val)
            node = node.right
        return ret          
'''
recursive
    def inorderTraversal(self, root):
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
'''