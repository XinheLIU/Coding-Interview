class Solution:
    def minWindow(self, s: 'str', t: 'str') -> 'str':
        # use a hash-table to store the number of appreances needed in target list
        if not s:
            return ""
        from collections import Counter
        # target count
        tcnt = Counter(t)
        targetUniqueL = len(tcnt)
        matched = 0
        # mapping count
        mcnt, n, j = Counter(), len(s), 0
        minL, minWindow = n + 1, ""
        # move the left pointer
        for i in range(n):
            # move in
            while j < n and matched < targetUniqueL:
                if s[j] in tcnt:
                    mcnt[s[j]] += 1
                    if mcnt[s[j]] == tcnt[s[j]]:
                        matched += 1
                j += 1
            
            # record/update min window
            if matched == targetUniqueL and j - i < minL:
                minL = j - i
                minWindow = s[i:j]
            # move out
            if s[i] in tcnt:
                if mcnt[s[i]] == tcnt[s[i]]:
                    matched -= 1
                mcnt[s[i]] -= 1    
        return minWindow