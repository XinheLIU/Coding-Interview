class Solution(object):
  def quickSort(self, array):
    """
    input: int[] array
    return: int[]
    """
    self.helper(array, 0, len(array) - 1)
    return array

  def helper(self, array, l, r):
      if l < r:
        pivot = self.partition(array, l, r)
        self.helper(array, l, pivot - 1)
        self.helper(array, pivot + 1, r)

  def partition(self, array, l, r):
      i, pivot = l-1, array[r]
      for j in range(l,r):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
      # put the pivot in place
      array[i+1], array[r] = array[r], array[i+1]
      return i+1