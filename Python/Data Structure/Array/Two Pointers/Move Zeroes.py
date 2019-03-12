class Solution(object):
  def moveZeroes(self, array):
    """
    input: int[] array
    return: int[]
    """
    if not array or not len(array):
      return array
    # two pointers
    i = 0
    for j in range(len(array)):
      if array[j] != 0:
        array[j], array[i] = array[i], array[j]
        i += 1