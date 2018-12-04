class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if(matrix == None or len(matrix) == 0 or len(matrix[0]) == 0):
            return False
        # fix the "upper right corner"
        nrow, ncol = len(matrix),len(matrix[0])
        row, col = 0, ncol - 1 # the upper right
        while row < nrow and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return False