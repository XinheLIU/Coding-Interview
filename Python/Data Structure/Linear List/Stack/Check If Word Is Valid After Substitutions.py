class Solution:
    def isValid(self, S: str) -> bool:
        if not S: return False
        stack = []
        word = "abc"
        for x in S:
            if x != "c":
                stack.append(x)
            else:
                if len(stack) < 2: return False
                if "".join([stack[-2], stack[-1], x]) != word:
                    return False
                stack.pop()
                stack.pop()
        return len(stack) == 0