class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        if not n: return 0
        if m < n: return -1
        for i in range(0, m - n + 1):
            if needle == haystack[i:i + n]:
                return i
        return -1
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        if not n: return 0
        if m < n: return -1
        for i in range(0, m - n + 1):
            j = 0
            while j < n:
                if needle[j] != haystack[i+j]: break
                j += 1
            if j == n: return i
        return -1
"""