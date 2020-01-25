class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        q = collections.deque([start])
        m, n = len(maze), len(maze[0])
        while q:
            i, j = q.popleft()
            maze[i][j] = 2
            if [i,j] == destination:
                return True
            for x, y in dirs:
                row = i + x
                col = j + y
                while 0 <= row < m and  0<= col < n and maze[row][col] != 1:
                    row += x
                    col += y
                row -= x
                col -= y
                if maze[row][col] == 0:
                    q.append((row, col))
        return False