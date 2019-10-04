# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        self.next = head
        prev, cur = self, head
        while cur and cur.next:
            temp = cur.next
            cur.next = cur.next.next
            temp.next = prev.next
            prev.next = temp
            # move forward
            prev, cur = cur, prev.next
        return self.next
        
'''
class Solution(object):
    # recursive
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        t = head.next
        # swap head and next
        t.next, head.next = head, self.swapPairs(head.next.next)
        return t
'''