class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        p_map = {")":"(", "]":"[","}":"{"}
        stack = []
        for c in s:
            if c not in p_map:
                stack.append(c)
            elif not stack or p_map[c] != stack.pop():
                return False
        return not stack