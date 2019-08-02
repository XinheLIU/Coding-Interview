"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        ret, stack = [], [root]
        while stack:
            p = stack.pop()
            ret.append(p.val)
            for c in p.children:
                stack.append(c)
        return ret[::-1]

"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ret = []
        if not root:
            return ret
        for child in root.children:
            ret += self.postorder(child)
        ret.append(root.val)
        return ret
"""