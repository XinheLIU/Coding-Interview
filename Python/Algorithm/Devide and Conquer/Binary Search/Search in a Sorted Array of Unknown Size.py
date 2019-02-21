# Definition for a unknown sized dictionary.
# class Dictionary(object):
#   def get(self, index):
#     pass
class Solution(object):
  def search(self, dic, target):
    """
    input: Dictionary dic, int target
    return: int
    """
    r = 1
    while dic.get(r) and dic.get(r) < target:
        r *= 2
    l = 0
    while l <= r:
        mid = l + (r - l) // 2
        if not dic.get(mid) or dic.get(mid) > target:
            r = mid - 1
        elif dic.get(mid) < target:
            l = mid + 1
        else:
            return mid
    return -1