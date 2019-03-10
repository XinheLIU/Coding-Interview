class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # bucket sort
        from collections import Counter
        cnt = Counter(nums)
        key, val = zip(*cnt.most_common(k))
        return key