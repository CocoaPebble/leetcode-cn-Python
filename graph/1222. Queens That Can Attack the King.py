'''
On a 0-indexed 8 x 8 chessboard, there can be multiple black queens ad one white king.

You are given a 2D integer array queens where queens[i] = [xQueeni, yQueeni] represents the position of the ith black queen on the chessboard. You are also given an integer array king of length 2 where king = [xKing, yKing] represents the position of the white king.

Return the coordinates of the black queens that can directly attack the king. You may return the answer in any order.
'''

from typing import List

class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        board = [[0] * 8 for _ in range(8)]
        for queen in queens:
            board[queen[0]][queen[1]] = 1

        def is_attack(king, queen):
            return king[0] == queen[0] or king[1] == queen[1] or abs(king[0] - queen[0]) == abs(king[1] - queen[1])
        
        def has_obstacle(king, queen):
            dx = 0 if king[0] == queen[0] else (1 if king[0] < queen[0] else -1)
            dy = 0 if king[1] == queen[1] else (1 if king[1] < queen[1] else -1)
            
            x, y = king[0] + dx, king[1] + dy
            
            while x != queen[0] or y != queen[1]:
                if board[x][y]:
                    return True
                x += dx
                y += dy
            
            return False

        res = []
        for queen in queens:
            if is_attack(king, queen) and not has_obstacle(king, queen):
                res.append(queen)
        
        return res

        