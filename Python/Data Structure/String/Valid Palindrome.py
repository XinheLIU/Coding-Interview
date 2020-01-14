class Solution:
  def isPalindrome(self, input: str) -> bool:
    """
    input: string input
    return: boolean
    """
    if not input:
      return True
    l, r = 0, len(input) - 1
    while l < r:
      if not input[l].isalnum():
        l += 1
      elif not input[r].isalnum():
        r -= 1
      else:
        if input[l].lower() != input[r].lower():
          return False
        l += 1
        r -= 1
    return True