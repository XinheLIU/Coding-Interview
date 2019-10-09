class Solution(object):
  def shortestDistance(self, words, word1, word2):
    """
    input: string[] words, string word1, string word2
    return: int
    """
    p1, p2 = -1, -1
    ret = float('inf')
    for i, word in enumerate(words):
      if word == word1:
        p1 = i
      elif word == word2:
        p2 = i
      if p1 != -1 and p2 != -1:
        ret = min(ret, abs(p1 - p2))
    return ret