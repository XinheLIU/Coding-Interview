#
# @lc app=leetcode id=692 lang=python3
#
# [692] Top K Frequent Words
#

# @lc code=start
import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = Counter(words)
        h = [(-freq, word) for word, freq in cnt.items()]
        heapq.heapify(h)
        return [heapq.heappop(h)[1] for _ in range(k)]
# @lc code=end

