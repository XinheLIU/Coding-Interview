from itertools import combinations
class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        # bitwise operation would be much faster
        def dfs(num, hours, res):
            if hours > num : return
            for hour in combinations([1, 2, 4, 8], hours):
                hs = sum(hour)
                if hs >= 12 : 
                    continue
                for minu in combinations([1, 2, 4, 8, 16, 32], num - hours):
                    mins = sum(minu)
                    if mins >= 60 : 
                        continue
                    res.append("%d:%02d" % (hs, mins))
            dfs(num, hours + 1, res)
        res = []
        dfs(num, 0, res)
        return res