class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # still the upper right corner
        if not matrix:
            return False
        nrow, ncol = len(matrix), len(matrix[0])
        row, col = 0, ncol - 1
        while row < nrow and col >= 0:
            val = matrix[row][col]
            if  val == target:
                return True
            elif val > target:
                col -= 1
            else:
                row += 1
        return False