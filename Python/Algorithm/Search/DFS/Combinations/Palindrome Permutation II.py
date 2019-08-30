class Solution:
    """
    @param s: the given string
    @return: all the palindromic permutations (without duplicates) of it
    """
    def generatePalindromes(self, s):
        # write your code here
        counter = collections.Counter(s)
        odds = filter(lambda x: x % 2, counter.values())
        if len(odds) > 1:
            return []
        baseStr, mid = self.preProcess(counter)
        return self.backTracking(baseStr, 0, mid, [baseStr + mid + baseStr[::-1]])
        
    def preProcess(self, counter):
        baseStr = mid = ""
        for char in counter:    
            if counter[char] % 2:
                mid = char
            baseStr += char*(counter[char]/2)
        return baseStr, mid
        
	# permutation of all left half is ok
    def backTracking(self, s, idx, mid, ans):
        if idx == len(s) - 1:
            return ans
        for i in range(idx, len(s)):
            if i >= 1 and s[i] == s[i-1] == s[idx]:
                continue #no need to go deeper if swap would be the same
            #Swap s[idx] with s[i]
            if i != idx:
                permu = s[:idx] + s[i] + s[idx+1:i] + s[idx] + s[i+1:] 
                ans.append(permu + mid + permu[::-1])
            else:
                permu = s
            self.backTracking(permu, idx+1, mid, ans)
        return ans