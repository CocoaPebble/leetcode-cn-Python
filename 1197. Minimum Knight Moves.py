'''
In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].

A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

'''

from typing import List
import collections

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        direction = [[1,2], [2,1], [2,-1], [1,-2], [-1,2], [-2,1], [-2,-1], [-1,-2]]

        q1, q2 = collections.deque([0, 0]), collections.deque([x, y])
        visited1, visited2 = set([0, 0]), set([x, y])
        ans = 0

        while q1 and q2:
            if len(q1) > len(q2):
                q1, q2 = q2, q1
                visited1, visited2 = visited2, visited1

            for i in range(len(q1)):
                cx, cy = q1.popleft()

                if [cx, cy] in visited2:
                    return ans

                for dx, dy in direction:
                    nx, ny = cx + dx, cy + dy
                    if [nx, ny] not in visited1:
                        visited1.add([nx, ny])
                        q1.append([nx, ny])
            
            ans += 1
            if ans > 0 and ans % 2 == 0:
                common = visited1 & visited2
                if common:
                    return ans // 2

        return ans
        
