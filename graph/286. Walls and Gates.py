'''
You are given an m x n grid rooms initialized with these three possible values.

-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

'''

from typing import List
import collections

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        m, n = len(rooms), len(rooms[0])

        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q = collections.deque()
                    q.append([i, j])

                    while q:
                        x, y = q.popleft()
                        for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < m and 0 <= ny < n and rooms[nx][ny] == 2147483647:
                                rooms[nx][ny] = rooms[x][y] + 1
                                q.append([nx, ny])

                            # if the distance to the gate is less than the current distance, update the distance
                            elif 0 <= nx < m and 0 <= ny < n and rooms[nx][ny] > rooms[x][y] + 1:
                                rooms[nx][ny] = rooms[x][y] + 1
                                q.append([nx, ny])

        return rooms