# Definition for a binary tree node with parent pointer.
# class TreeNodeP(object):
#     def __init__(self, x, p):
#         self.value = x
#         self.left = None
#         self.right = None
#         self.parent = p

class Solution(object):
  def lowestCommonAncestor(self, one, two):
    """
    input: TreeNodeP one, TreeNodeP two
    return: TreeNodeP
    """
    # you don't have the root
    if not one or not two: return None
    parents_one = set()
    while one:
      parents_one.add(one)
      one = one.parent
    while two:
      if two in parents_one:
        return two
      two = two.parent
    return None