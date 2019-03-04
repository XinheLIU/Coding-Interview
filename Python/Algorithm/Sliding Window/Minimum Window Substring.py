class Solution:
    def getMap(self, target):
        map = {}
        for c in target:
            map[c] = map.get(c,0) + 1
        return map
    
    def minWindow(self, s: 'str', t: 'str') -> 'str':
        # use a hash-table to store the number of appreances needed in target list
        if not s:
            return ""
        map = self.getMap(t)
        targetUniqueL = len(map)
        matched = 0
        # use another map to check if we matched (or we can do -= 1 on original map)
        hash, n, j = {}, len(s), 0
        minL, minWindow = n + 1, ""
        # move the left pointer
        for i in range(n):
            # move the right pointer
            while j < n and matched < targetUniqueL:
                if s[j] in map:
                    hash[s[j]] = hash.get(s[j], 0) + 1
                    if hash[s[j]] == map[s[j]]:
                        matched += 1
                j += 1
            
            # record/update min window
            if matched == targetUniqueL and j - i < minL:
                minL = j - i
                minWindow = s[i:j]
            # record the left pointer move
            if s[i] in map:
                if hash[s[i]] == map[s[i]]:
                    matched -= 1
                hash[s[i]] -= 1
    
        return minWindow