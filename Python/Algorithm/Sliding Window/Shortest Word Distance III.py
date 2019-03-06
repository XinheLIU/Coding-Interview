class Solution(object):
  def shortestWordDistance(self, words, word1, word2):
    """
    input: string[] words, string word1, string word2
    return: int
    """
    # last apperance 
    idx, ret = -1, float('inf')
    for i, word in enumerate(words):
      if word == word1 or word == word2:
        if idx != -1 and (word1 == word2 or word != words[idx]):
          ret = min(ret, i - idx)
        idx = i
    return ret