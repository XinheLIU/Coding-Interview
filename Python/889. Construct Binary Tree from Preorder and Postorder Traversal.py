# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if not pre:
            return None
        root = TreeNode(pre[0])
        if len(pre) == 1:
            return root
        L = post.index(pre[1]) + 1 # size of left subtree
        root.left, root.right = self.constructFromPrePost(pre[1:L+1], post[:L]), self.constructFromPrePost(pre[L+1:], post[L:-1])
        return root