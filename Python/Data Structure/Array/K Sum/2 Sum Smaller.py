class Solution(object):
  def smallerPairs(self, nums, target):
    """
    input: int[] array, int target
    return: int
    """
    ret = 0
    if not nums:
      return ret
    nums.sort()
    for i in range(len(nums) -1, 0, -1):
      if nums[i] > target:
        continue
      for j in range(0, i):
        if nums[i] + nums[j] < target:
          ret += 1
    return ret