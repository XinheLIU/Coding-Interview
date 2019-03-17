class Solution:
    def firstOccur(self, array, target):
        if not array or len(array) == 0:
            return - 1
        l, r = 0, len(array) - 1
        while l + 1 < r:
            mid = l + (r - l) // 2
            if array[mid] < target:
                l = mid + 1
            elif array[mid] >= target:
                 r = mid
        if array[l] == target:
            return l
        elif array[r] == target:
            return r
        else:
            return -1

    def lastOccur(self, array, target):
        if not array or len(array) == 0:
            return - 1
        l, r = 0, len(array) - 1
        while l + 1 < r:
            mid = l + (r - l) // 2
            if array[mid] <= target:
                l = mid
            elif array[mid] > target:
                r = mid - 1
        if array[r] == target:
            return r
        elif array[l] == target:
            return l
        else:
            return -1

    def searchRange(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        l, r = self.firstOccur(nums, target), self.lastOccur(nums, target)
        return [l, r]