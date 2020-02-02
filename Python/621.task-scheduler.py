#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#

# @lc code=start
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
       cnt = collections.Counter(tasks)
       counts = list(cnt.values())
       longest = max(counts) 
       return max((longest - 1)  * (n + 1) + counts.count(longest), len(tasks))
# @lc code=end

