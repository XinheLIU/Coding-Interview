# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        # how to count
        points, cnt = set(G), 0
        while head:
            if head.val in points and (not head.next or head.next.val not in points):
                    cnt += 1
            head = head.next
        return cnt