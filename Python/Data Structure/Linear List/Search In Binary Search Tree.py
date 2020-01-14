# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
  def search(self, root, key):
    """
    input: TreeNode root, int key
    return: TreeNode
    """
    if not root:
      return None
    if root.val == key:
      return root
    elif root.left and root.val > key:
      return self.search(root.left, key)
    elif root.right and root.val < key:
      return self.search(root.right, key)
    return None