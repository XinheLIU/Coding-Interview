class Solution:
    # O(N) solution
    def maxChunksToSorted(self, arr: List[int]) -> int:
        ret, n, f, b = 1, len(arr), arr[:], arr[:]
        # f: forward array = max(arr[:i]), b: backward array: min(arr[i:])
        for i in range(1, n):
            f[i] = max(arr[i], f[i-1])
        for i in range(n-2, -1, -1):
            b[i] = min(arr[i], b[i+1])
        for i in range(n-1):
            if f[i] <= b[i+1]:
                ret += 1
        return ret
        
"""
# O(Nlog N) Solutions
# sliding window
class Solution(object):
    def maxChunksToSorted(self, arr):
        count = collections.defaultdict(int)
        ans = nonzero = 0

        for x, y in zip(arr, sorted(arr))
            count[x] += 1
            if count[x] == 0: nonzero -= 1
            if count[x] == 1: nonzero += 1

            count[y] -= 1
            if count[y] == -1: nonzero += 1
            if count[y] == 0: nonzero -= 1

            if nonzero == 0: ans += 1

        return ans


# sorted count pairs

class Solution(object):
    def maxChunksToSorted(self, arr):
        count = collections.Counter()
        counted = []
        for x in arr:
            count[x] += 1
            counted.append((x, count[x]))

        ans, cur = 0, None
        for X, Y in zip(counted, sorted(counted)):
            cur = max(cur, X)
            if cur == Y:
                ans += 1
        return ans
        
"""
