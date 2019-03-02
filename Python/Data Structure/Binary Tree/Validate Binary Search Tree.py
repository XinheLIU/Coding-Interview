class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isValid(root, minv, maxv):
            if not root:
                return True
            if root.val <= minv or root.val >= maxv:
                return False
            return isValid(root.left, minv, root.val) and isValid(root.right,root.val,maxv)
        return isValid(root, float('-inf'), float('inf'))