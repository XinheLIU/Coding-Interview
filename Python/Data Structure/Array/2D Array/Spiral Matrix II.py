class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        up, down, left, right = 0, n - 1, 0, n - 1
        matrix = [[0 for i in range(n)] for j in range(n)]
        direct, count = 0, 1 # 0: right, 1: down, 2: left, 3: up
        while True:
            if direct == 0:
                for i in range(left, right + 1):
                    matrix[up][i] = count
                    count += 1
                up += 1
            elif direct == 1:
                for i in range(up, down + 1):
                    matrix[i][right] = count
                    count += 1
                right -= 1
            elif direct == 2:
                for i in range(right, left - 1, -1):
                    matrix[down][i] = count
                    count += 1
                down -= 1
            elif direct == 3:
                for i in range(down, up - 1, -1):
                    matrix[i][left] = count 
                    count += 1
                left += 1
            if up > down or left > right:
                return matrix
            direct = (direct + 1) % 4