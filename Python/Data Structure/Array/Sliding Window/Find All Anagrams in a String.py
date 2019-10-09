from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ret = []
        if not s or not p:
            return ret
        if len(s) < len(p):
            return ret
        cnt, n = Counter(p), len(p)
        match = len(cnt)
        for i, letter in enumerate(s):
            if letter in cnt:
                cnt[letter] -= 1
                if cnt[letter] == 0:
                    match -= 1
            if i >= n:
                left_l = s[i-n] # move out
                if left_l in cnt:
                    cnt[left_l] += 1
                    if cnt[left_l] == 1:
                        match += 1
            if match == 0:
                ret.append(i-n+1)
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