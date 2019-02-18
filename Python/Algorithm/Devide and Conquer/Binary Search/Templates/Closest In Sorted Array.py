class Solution(object):
  def closest(self, array, target):
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
      if array[mid] == target:
        return mid
      elif array[mid] < target:
          l = mid
      else:
          r = mid
    return l if abs(array[l] - target) <= abs(array[r] - target) else r