class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ret = []
        if not s or not p:
            return ret
        if len(p) > len(s):
            return ret
        from collections import Counter
        cnt, k = Counter(p), len(p)
        match = len(cnt) # num of char match needed
        # sliding window of size k
        for i, letter in enumerate(s):
            # move in
            if letter in cnt:
                cnt[letter] -= 1        
                if cnt[letter] == 0: # matched
                    match -= 1                
            if i >= k:
                # move out
                l = s[i - k] # left letter to move out
                if l in cnt:
                    cnt[l] += 1
                    if cnt[l] == 1: # new match needed
                        match += 1
            if match == 0:
                ret.append(i - k + 1)
        return ret

'''
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ret = []
        if not s or not p:
            return ret
        if len(p) > len(s):
            return ret
        cnt = self.countmap(p)
        match = 0  # num of char matched
        # sliding window of size p length
        for i in range(len(s)):
            # move in
            letter = s[i]
            if letter in cnt:
                cnt[letter] -= 1        
                if cnt[letter] == 0:
                    match += 1                
            if i >= len(p):
                # move out
                temp = s[i - len(p)]
                if temp in cnt:
                    cnt[temp] += 1
                    if cnt[temp] == 1:
                        match -= 1
            if match == len(cnt):
                ret.append(i - len(p) + 1)
        return ret
    
    def countmap(self, sh):
        dic = {}
        for letter in sh:
            if letter in dic:
                dic[letter] += 1
            else:
                dic[letter] = 1
        return dic
'''