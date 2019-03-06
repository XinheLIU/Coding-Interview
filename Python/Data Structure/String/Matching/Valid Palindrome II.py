class Solution:
  def valid(self, input):
    """
    input: string input
    return: boolean
    """
    l, r = 0, len(input) - 1
    while l < r:
      if input[l]!= input[r]:
        return False
      l += 1
      r -= 1
    return True
  
  def validPalindrome(self, input: str) -> bool:
    """
    input: string input
    return: boolean
    """
    if not input:
      return True
    l, r = 0, len(input) - 1
    while l < r:
      if input[l] != input[r]:
        return self.valid(input[:l] + input[l+1:]) or self.valid(input[:r] + input[r+1:])
      l += 1
      r -= 1
    return True