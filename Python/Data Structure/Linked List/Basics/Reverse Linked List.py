# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # iterative solution
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur, prev = head, None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev
    
    ''' normal (no-python) solution 
    def reverseList(self, head):
    	prev = None
    	while head:
    		next = node.next
    		node.next = prev
    		prev = node
    		node = next
    	return prevN
    '''

    '''
    # recursive solution
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        p = head
        head = self.reverseList(p.next)
        p.next.next, p.next = p, None
        return head
    '''