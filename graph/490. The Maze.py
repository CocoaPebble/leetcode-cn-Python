'''
There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1). The ball can go through the empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the m x n maze, the ball's start position and the destination, where start = [startrow, startcol] and destination = [destinationrow, destinationcol], return true if the ball can stop at the destination, otherwise return false.

You may assume that the borders of the maze are all walls (see examples).

'''

from typing import List
import collections

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        # BFS

        m, n = len(maze), len(maze[0])
        q = collections.deque()
        q.append(start)
        visited = [[0] * n for _ in range(m)]
        visited[start[0]][start[1]] = 1

        while q:
            x, y = q.popleft()
            if [x, y] == destination:
                return True
            
            for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                nx, ny = x, y
                while 0 <= nx + dx < m and 0 <= ny + dy < n and maze[nx + dx][ny + dy] == 0:
                    nx += dx
                    ny += dy
                
                if not visited[nx][ny]:
                    visited[nx][ny] = 1
                    q.append([nx, ny])
                
        return False