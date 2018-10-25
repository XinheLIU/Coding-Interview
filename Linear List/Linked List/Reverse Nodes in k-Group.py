# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverse(self, head, tail):
        pre = tail
        # move nodes after cur to after prev one by one 
        while head is not tail:
            head.next, pre, head = pre, head, head.next
        return pre
    
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        cur = head
        for i in range(k):
            if not cur:
                return head
            cur = cur.next
        new_head = self.reverse(head, cur)
        # head now is the thing before last
        head.next = self.reverseKGroup(cur, k)
        return new_head
'''
class Solution(object):
    def reverseKNodes(self, prev, k):
        prev, cur = prev, prev.next
        # move nodes after cur to after prev one by one 
        for i in range(k-1):
            temp, cur.next = cur.next, cur.next.next
            temp.next, prev.next  = prev.next, temp
        return cur
    
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """ 
        self.next = head
        prev, cur = self, self.next
        i = 0
        while cur:
            i += 1
            if i % k == 0:
                prev = self.reverseKNodes(prev, k)
                cur  = prev.next
            else:
                cur = cur.next
        return self.next
'''    