class Solution(object):
  def rotate(self, matrix):
    """
    input: int[][] matrix
    return: No need to return
    """
    # many methods
    n = len(matrix)
    for i in range(n):
      for j in range(i+1, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
      matrix[i].reverse()