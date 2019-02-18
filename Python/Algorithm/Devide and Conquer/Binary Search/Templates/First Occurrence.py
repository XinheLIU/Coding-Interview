class Solution(object):
  def firstOccur(self, array, target):
    """
    input: int[] array, int target
    return: int
    """
    # write your solution here
    if not array or len(array) == 0:
      return - 1
    l, r = 0, len(array) - 1
    while l + 1 < r:
      mid = l + (r - l) // 2
      if array[mid] < target:
          l = mid
      elif array[mid] >= target:
          r = mid
    if array[l] == target:
      return l
    elif array[r] == target:
      return r
    else:
      return -1