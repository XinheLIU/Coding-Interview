class Solution:
    def containsNearbyDuplicate(self, nums, k):
        map = {}
        for j, num in enumerate(nums):
            if num in map:
                if j - map[num] <= k:
                    return True
            map[num] = j
        return False