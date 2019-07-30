class Solution(object):
  """
  k buckets(a sliding window of size k), chek +-1 buckets
  If | nums[i] - nums[j] | <= t   a

  then： | nums[i] / t - nums[j] / t | <= 1   b

    | floor(nums[i] / t) - floor(nums[j] / t) | <= 1   c

   floor(nums[j] / t) ∈ {floor(nums[i] / t) - 1, floor(nums[i] / t), floor(nums[i] / t) + 1}  d
  """
  def containsNearbyAlmostDuplicate(self, nums, k, t):
    """
    input: int[] nums, int k, int t
    return: boolean
    """
    from collections import OrderedDict
    if k < 1 or t < 0:
      return False
    buckets = OrderedDict()
    for i, num in enumerate(nums):
      key = num // max(1, t)
      for m in (key, key - 1, key + 1):
        if m in buckets and abs(num - buckets[m]) <= t:
          return True
      buckets[key] = num
      if i >= k:  # nums[i-k] corresponding value
        buckets.popitem(last=False)
    return False