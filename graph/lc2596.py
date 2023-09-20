'''
    There is a knight on an n x n chessboard. In a valid configuration, the knight starts at the top-left cell of the board and visits every cell on the board exactly once.

You are given an n x n integer matrix grid consisting of distinct integers from the range [0, n * n - 1] where grid[row][col] indicates that the cell (row, col) is the grid[row][col]th cell that the knight visited. The moves are 0-indexed.

Return true if grid represents a valid configuration of the knight's movements or false otherwise.

Note that a valid knight move consists of moving two squares vertically and one square horizontally, or two squares horizontally and one square vertically. The figure below illustrates all the possible eight moves of a knight from some cell.
'''



class Solution:
    def checkValidGrid(self, grid: list[list[int]]) -> bool:
        m,n = len(grid),len(grid[0])
        visited = [[False]*n for _ in range(m)]
        direction = [[-2,1],[-2,-1],[-1,2],[-1,-2],[1,2],[1,-2],[2,1],[2,-1]]

        def dfs(i, j):
            visited[i][j] = True
            for d in direction:
                x, y = i + d[0], j + d[1]
                if 0 <= x < m and 0 <= y < n and not visited[x][y]:
                    if grid[x][y] == grid[i][j] + 1:
                        dfs(x, y)
                        return True
            return

        dfs(0, 0)
        return all([all(row) for row in visited])
        