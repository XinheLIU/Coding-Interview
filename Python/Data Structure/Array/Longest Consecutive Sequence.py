class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # use a set
        ret, num_set = 0, set(nums)
        for num in nums:
            if num not in num_set:
                continue
            num_set.remove(num)
            pre, nxt = num - 1, num + 1
            while pre in num_set:
                num_set.remove(pre)
                pre -= 1
            while nxt in num_set:
                num_set.remove(nxt)
                nxt += 1
            ret = max(ret, nxt - pre - 1)
        return ret
"""
class Solution:
    def longestConsecutive(self, nums):
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak
"""