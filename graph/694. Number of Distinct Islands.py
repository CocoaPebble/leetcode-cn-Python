'''
company
彭博 Bloomberg
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

Return the number of distinct islands.
'''

from typing import List

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        shape = set()

        def dfs(x, y, previous_path):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0:
                return
            
            grid[x][y] = 0
            previous_path.append((x, y))

            dfs(x + 1, y, previous_path)
            dfs(x - 1, y, previous_path)
            dfs(x, y + 1, previous_path)
            dfs(x, y - 1, previous_path)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    path = []
                    start_x, start_y = i, j
                    dfs(i, j, path)

                    for i in range(len(path)):
                        path[i] = (path[i][0] - start_x, path[i][1] - start_y)

                    shape.add(tuple(path))
        
        return len(shape)
