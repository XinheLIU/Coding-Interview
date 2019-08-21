class Solution:
    # brute force, can use KMP
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(n // 2 , 0, -1):
            if n % i == 0:
                c = n // i
                t = s[:i] * c
                if t == s:
                    return True
        return False