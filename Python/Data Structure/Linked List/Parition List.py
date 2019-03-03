class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        # do the problem in place
        # find the first >= x value, move others before it
        dummy = ListNode(None)
        dummy.next = head
        prev, cur = dummy, head
        while(prev.next and prev.next.val < x ):
            prev = prev.next
        # now prev.next >= x, move others before it
        cur = prev
        while(cur.next):
            if cur.next.val < x:
                temp = cur.next
                cur.next = temp.next
                temp.next = prev.next
                prev.next = temp
                prev = prev.next
            else:
                cur = cur.next
        return head
        '''
    def partition(self, head, x):
        # do the problem by creating a new one than link oringinal at the end
        dummy, dummy2 = ListNode(None), ListNode(None)
        dummy.next = head
        cur = dummy
        p = dummy2
        # cur < x, move to the back 
        while(cur.next):
            if cur.next.val < x:
                p.next = cur.next
                cur.next = cur.next.next
                p = p.next
                p.next = None 
            else:
                cur = cur.next
        # Linked to the back
        p.next = dummy.next        
        return dummy2.next
		'''