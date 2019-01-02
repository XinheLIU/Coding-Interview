# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        # use a tag in the stack to see where the node comes back from or use a pre node
        ret, stack, p, pre = [],[root],root, TreeNode(None) # pre is the last visited node
        while len(stack):
            p = stack[-1]
            if (not p.left and not p.right) or (pre and (pre == p.left or pre == p.right)):
                ret.append(p.val)
                stack.pop()
                pre = p
            else:
                if p.right:
                    stack.append(p.right)
                if p.left:
                    stack.append(p.left)
        return ret
'''
    def postorderTraversal(self, root):
        if not root:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
'''