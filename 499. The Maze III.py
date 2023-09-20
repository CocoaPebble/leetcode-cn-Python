'''
There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1). The ball can go through the empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction. There is also a hole in this maze. The ball will drop into the hole if it rolls onto the hole.

Given the m x n maze, the ball's position ball and the hole's position hole, where ball = [ballrow, ballcol] and hole = [holerow, holecol], return a string instructions of all the instructions that the ball should follow to drop in the hole with the shortest distance possible. If there are multiple valid instructions, return the lexicographically minimum one. If the ball can't drop in the hole, return "impossible".

If there is a way for the ball to drop in the hole, the answer instructions should contain the characters 'u' (i.e., up), 'd' (i.e., down), 'l' (i.e., left), and 'r' (i.e., right).

The distance is the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included).

You may assume that the borders of the maze are all walls (see examples).
'''


from typing import List
import collections

class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        # BFS

        m, n = len(maze), len(maze[0])
        q = collections.deque()
        q.append(ball)

        dist = [[float('inf')] * n for _ in range(m)]
        dist[ball[0]][ball[1]] = 0
        path = [['impossible'] * n for _ in range(m)]
        path[ball[0]][ball[1]] = ''

        while q:
            x, y = q.popleft()

            for dx, dy, d in [[0, 1, 'r'], [0, -1, 'l'], [1, 0, 'd'], [-1, 0, 'u']]:
                nx, ny, step, p = x + dx, y + dy, dist[x][y] + 1, path[x][y] + d

                while 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == 0 and not(nx - dx == hole[0] and ny -dy == hole[1]):
                    nx += dx
                    ny += dy
                    step += 1
                
                nx -= dx
                ny -= dy
                step -= 1

                if step < dist[nx][ny] or (step == dist[nx][ny] and p < path[nx][ny]):
                    dist[nx][ny] = step
                    path[nx][ny] = p
                    if not (nx == hole[0] and ny == hole[1]):
                        q.append([nx, ny])    

        return path[hole[0]][hole[1]]
                    

                    
