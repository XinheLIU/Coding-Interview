class Solution(object):
  def sort(self, array):
    """
    input: int[] array
    return: int[]
    """
    # sort it in place
    for i in range(1, len(array)):
      cur, k = array[i], i
      while k > 0 and array[k-1] > cur:
        array[k] = array[k-1]
        k -= 1
      array[k] = cur
    return array