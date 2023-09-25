'''
There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1). The ball can go through the empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the m x n maze, the ball's start position and the destination, where start = [startrow, startcol] and destination = [destinationrow, destinationcol], return the shortest distance for the ball to stop at the destination. If the ball cannot stop at destination, return -1.

The distance is the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included).

You may assume that the borders of the maze are all walls (see examples).
'''


from typing import List
import collections

class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        # BFS

        m, n = len(maze), len(maze[0])
        q = collections.deque()
        q.append(start)
        visited = [[float('inf')] * n for _ in range(m)]
        visited[start[0]][start[1]] = 0

        while q:
            x, y = q.popleft()
            # if [x, y] == destination:
            #     return visited[x][y]
            
            for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                nx, ny = x, y
                step = 0
                while 0 <= nx + dx < m and 0 <= ny + dy < n and maze[nx + dx][ny + dy] == 0:
                    nx += dx
                    ny += dy
                    step += 1
                
                if visited[x][y] + step < visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + step
                    q.append([nx, ny])
                
        return visited[destination[0]][destination[1]] if visited[destination[0]][destination[1]] != float('inf') else -1