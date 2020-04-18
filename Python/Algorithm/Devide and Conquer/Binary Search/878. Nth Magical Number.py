class Solution:
    def nthMagicalNumber(self, N: int, A: int, B: int) -> int:
        from fractions import gcd
        MOD = 10 ** 9 + 7
        L = A / gcd(A, B) * B
        
        def count_leq(x):
            return x // A + x // B - x // L
        
        l, r = 0, 10 ** 15
        while l < r:
            mid = l + ((r - l) >> 1)
            if count_leq(mid) < N:
                l = mid + 1
            else:
                r = mid
        return l % MOD