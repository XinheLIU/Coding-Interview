class Solution(object):
  def isAnagram(self, source, target):
    """
    input: string source, string target
    return: boolean
    """
    if len(source) != len(target): return False
    # you can use Counter directly, but here we use dict
    map = [0] * 26
    for c in source:
      map[ord(c) - ord('a')] += 1
    for c in target:
      map[ord(c) - ord('a')]  -= 1
      if map[ord(c) - ord('a')] < 0:
        return False
    return True