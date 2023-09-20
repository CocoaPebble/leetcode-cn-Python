'''
You are given an m x n grid grid of values 0, 1, or 2, where:

each 0 marks an empty land that you can pass by freely,
each 1 marks a building that you cannot pass through, and
each 2 marks an obstacle that you cannot pass through.
You want to build a house on an empty land that reaches all buildings in the shortest total travel distance. You can only move up, down, left, and right.

Return the shortest travel distance for such a house. If it is not possible to build such a house according to the above rules, return -1.

The total travel distance is the sum of the distances between the houses of the friends and the meeting point.

The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

'''

from typing import List
import collections

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        buildings = 0
        distances = [[0] * n for _ in range(m)]
        reach = [[0] * n for _ in range(m)]

        def bfs(i, j):
            visited = [[False] * n for _ in range(m)]
            visited[i][j] = True
            queue = collections.deque([(i, j, 0)])
            while queue:
                i, j, dist = queue.popleft()
                for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                    if 0 <= x < m and 0 <= y < n and not visited[x][y]:
                        visited[x][y] = True
                        if grid[x][y] == 0:
                            distances[x][y] += dist + 1
                            reach[x][y] += 1
                            queue.append((x, y, dist + 1))
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    bfs(i, j)
                    buildings += 1
        
        ans = float('inf')
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and reach[i][j] == buildings:
                    ans = min(ans, distances[i][j])
        
        return ans if ans != float('inf') else -1
