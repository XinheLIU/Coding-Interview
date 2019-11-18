class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret, start,stack = 0,0,[] 
        for i in range(len(s)):
            c = s[i]
            if c == '(':
                stack.append(i)
            else:
                if not stack:
                    start = i + 1
                else:
                    stack.pop()
                    if stack:
                        ret = max(ret, i - stack[-1])
                    else:
                        ret = max(ret, i - start + 1)
        return ret