# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        # fast slow pointers
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        fast, slow, prev = head, head, head
        while fast.next and fast.next.next:
            prev = slow
            fast, slow = fast.next.next, slow.next
        #slow is the mid
        root = TreeNode(slow.val)
        fast, prev.next = slow.next, None
        root.left   = self.sortedListToBST(head) if slow != head else None   # two nodes, first root, second right child
        root.right  = self.sortedListToBST(fast)
        return root