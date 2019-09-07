class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        ns = sorted([(d[0], i) for i, d in enumerate(intervals)])
        res = []
        for d in intervals:
            n = d[1]
            if n > ns[-1][0]:
                res.append(-1)
            elif n <= ns[0][0]:
                res.append(ns[0][1])
            else:
                l, r = 0, len(ns)-1
                while r - l > 1:
                    m = (r + l) >> 1
                    if ns[m][0] >= n:
                        r = m
                    else:
                        l = m
                res.append(ns[r][1])
        return res