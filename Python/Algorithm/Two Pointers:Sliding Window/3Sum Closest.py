class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closest = sum(nums[0:3])
        length, diff = len(nums), abs(closest - target)
        for i in range(0, length - 2):
            left, right = i + 1, length - 1
            while left < right:
                Sum = nums[i] + nums[left] + nums[right]
                new_diff = abs(Sum - target)
                if new_diff < diff:
                    diff = new_diff
                    closest = Sum
                if Sum < target:
                    left += 1
                else:
                    right -= 1
        return closest