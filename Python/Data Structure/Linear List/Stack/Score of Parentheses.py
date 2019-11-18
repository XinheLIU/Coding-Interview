class Solution:
    # many methods we can do this
    def scoreOfParentheses(self, S: str) -> int:
        stack = [0]
        for x in S:
            if x == "(":
                stack.append(0)
            else:
                top = stack.pop()
                if top == 0:
                    stack[-1] += 1
                else:
                    stack[-1] += top * 2
        return stack[-1]