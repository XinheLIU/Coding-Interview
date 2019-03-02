class Solution(object):
  def evalRPN(self, tokens):
    """
    input: string[] tokens
    return: int
    """
    import operator as ops
    stack, map = [], {"+": ops.add, "-": ops.sub, "*": ops.mul, "/":ops.truediv}
    for s in tokens:
      if s in map:
        r = stack.pop()
        l = stack.pop()
        stack.append(int(map[s](l,r)))
      else:
        stack.append(int(s))
    return stack[0]