# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
  def closest(self, root, target):
    """
    input: TreeNode root, int target
    return: int
    """
    ret = root.val
    if root.left and root.val > target:
      l = self.closest(root.left, target)
      if abs(ret - target) > abs(l - target):
        ret = l
    if root.right and root.right > target:
      r = self.closest(root.right, target)
      if abs(ret - target) > abs(r - target):
        ret = r
    return ret