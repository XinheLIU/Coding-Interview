#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
            if slow is fast:
                break
        if fast is None or fast.next is None: 
            return None
        slow = head
        while slow is not fast:
            fast, slow = fast.next, slow.next
        return fast
# @lc code=end

