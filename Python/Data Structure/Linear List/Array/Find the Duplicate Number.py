class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break
        # find entrance
        t = 0
        while True:
            slow = nums[slow]
            t = nums[t]
            if slow == t: break
        return slow