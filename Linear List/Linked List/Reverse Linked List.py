class Solution(object):
    # iterative solution
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
                return head
        prev = ListNode(None)
        prev.next = head
        cur = head
        while(cur.next):
                temp = cur.next
                cur.next = temp.next
                temp.next = prev.next
                prev.next = temp
        return prev.next
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
        p.next.next = p
        p.next = None
        return head
    '''
