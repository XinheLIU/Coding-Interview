# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

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
    # non-recursive
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev, self.next, cur = self, head, head
        while cur and cur.next:
            temp, cur.next = cur.next, cur.next.next
            temp.next, prev.next = prev.next, temp
            prev, cur = cur, cur.next  #moved two steps from original 
        return self.next 
    '''