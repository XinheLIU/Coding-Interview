class Solution(object):
  def search(self, A, target):
    """
    input: int[] array, int target
    return: int
    """
    if not A:
        return -1
    l, r = 0, len(A) - 1
    while l + 1 < r:
        mid = l + (r - l ) // 2
        if A[mid] >= A[l]:
            # left is ordered
            if A[l] <= target <= A[mid]:
                r = mid
            else:
                l = mid
        else:
            # right is ordered
            if A[mid] <= target <= A[r]:
                l = mid
            else:
                r = mid
    if A[l] == target:
        return l
    if A[r] == target:
        return r
    return -1