# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        pre, stack, ret = None, [root], []
        while len(stack):
            p = stack[-1]
            if (not p.right and not p.left) or (pre and (pre == p.left or pre == p.right)):
                ret.append(p.val)
                stack.pop()
                pre = p
            else:
                if p.right: stack.append(p.right)
                if p.left: stack.append(p.left)
        return ret
'''
    def postorderTraversal(self, root):
        if not root:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
'''