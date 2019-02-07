class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]
    
    '''
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not len(s):
            return ''
        l, r = 0, len(s)-1
        ss = ['']*len(s)
        while l < r:
            ss[l],ss[r] = s[r],s[l]
            l, r = l+1, r-1
        if l == r:
            ss[l] = s[r]
        return ''.join(ss)
    '''
    '''
     def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: void Do not return anything, modify s in-place instead.
        """
        def helper(start, end, ls):
            if start >= end:
                return
        
            # swap the first and last element
            ls[start], ls[end] = ls[end], ls[start]        

            return helper(start+1, end-1, ls)
    
        helper(0, len(s)-1, s)
    '''