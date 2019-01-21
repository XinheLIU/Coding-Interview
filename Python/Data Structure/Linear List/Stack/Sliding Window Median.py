import bisect
class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        n = len(nums)
        if n == 0:
            return []
        arr = []
        [arr.insert(bisect.bisect_left(arr, v), v) for v in nums[:k]]
        res = [self.getMedian(arr)]
        i = 0
        for v in nums[k:]:
            index = bisect.bisect_left(arr, nums[i])
            arr = arr[:index] + arr[index+1:]
            index = bisect.bisect_left(arr, v)
            arr.insert(index, v)
            i += 1
            res.append(self.getMedian(arr))
        return res

    def getMedian(self, arr):
        n = len(arr)
        return (arr[n//2]+arr[n//2-1]) / 2.0 if n % 2 == 0 else arr[n//2] * 1.0