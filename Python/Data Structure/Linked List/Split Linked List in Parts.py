# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, root: 'ListNode', k: 'int') -> 'List[ListNode]':
        # total lengeth
        p, N = root, 0
        while p:
            p = p.next
            N += 1
        width, res = divmod(N,k)
        ret = []
        p = root
        for i in range(k):
            head = write = ListNode(None)
            for j in range(width + (i < res)):
                write.next = write = ListNode(p.val)
                if p: p = p.next
            ret.append(head.next)
        return ret