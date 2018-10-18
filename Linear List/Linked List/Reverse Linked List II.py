class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head
        cur = dummy
        for i in range(1,m):
            cur = cur.next
        prev = cur
        cur = cur.next
        # move nodes after cur to after prev one by one 
        for i in range(n-m):
            temp = cur.next
            cur.next = cur.next.next
            temp.next = prev.next
            prev.next = temp
        return dummy.next