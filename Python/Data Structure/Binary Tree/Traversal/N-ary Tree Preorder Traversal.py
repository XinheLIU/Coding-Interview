"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        ret, stack = [], [root]
        while stack:
            p = stack.pop()
            ret.append(p.val)
            for c in p.children[::-1]:
                stack.append(c)
        return ret
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ret = []
        
        def helper(root, ret):
            if not root:
                return
            ret.append(root.val)
            for c in root.children:
                helper(c, ret)
        helper(root, ret)
        return ret
"""