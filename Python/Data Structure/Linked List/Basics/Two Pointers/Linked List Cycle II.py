# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return None
        # fast : a + b(cycle start) + c(slow riched cycle) + b
        # slow: a + b
        fast = slow = head 
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow is fast:
                break
        if slow is fast:
            slow = head
            while slow is not fast:
                slow, fast = slow.next, fast.next
            return slow
        return None