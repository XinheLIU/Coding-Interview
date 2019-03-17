class Solution(object):
  def lastOccur(self, array, target):
    """
    input: int[] array, int target
    return: int
    """
    if not array or len(array) == 0:
      return - 1
    l, r = 0, len(array) - 1
    while l + 1 < r:
      mid = l + (r - l) // 2
      if array[mid] <= target:
          l = mid
      elif array[mid] > target:
          r = mid
    if array[r] == target:
      return r
    elif array[l] == target:
      return l
    else:
      return -1