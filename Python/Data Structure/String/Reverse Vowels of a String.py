class Solution:
  def reverseVowels(self, s: str) -> str:
    """
    s: string input
    return: string
    """
    if not s:
      return s
    vowels = set('aeiou'.upper() + 'aeiou')
    ss = list(s)
    l, r = 0, len(ss) - 1
    while l < r:
      if ss[l] not in vowels:
        l += 1
      elif ss[r] not in vowels:
        r -= 1
      else:
        ss[l], ss[r] = ss[r], ss[l]
        l += 1
        r -= 1
    return ''.join(ss)