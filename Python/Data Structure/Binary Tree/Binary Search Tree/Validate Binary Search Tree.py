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

'''
# in order traversal
class Solution(object):
    def validBSTHelper(self, root):
        if not root:
            return True

        res = self.validBSTHelper(root.left)

        if not self.prev:
            self.prev = root
        else:
            if root.val <= self.prev.val:
                res = False
            self.prev = root

        res = res and self.validBSTHelper(root.right)

        return res

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.prev = None
        return self.validBSTHelper(root) 
'''