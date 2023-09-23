'''
There exists an undirected and unrooted tree with n nodes indexed from 0 to n - 1. You are given an integer n and a 2D integer array edges of length n - 1, where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree. You are also given an array coins of size n where coins[i] can be either 0 or 1, where 1 indicates the presence of a coin in the vertex i.

Initially, you choose to start at any vertex in the tree. Then, you can perform the following operations any number of times: 

Collect all the coins that are at a distance of at most 2 from the current vertex, or
Move to any adjacent vertex in the tree.
Find the minimum number of edges you need to go through to collect all the coins and go back to the initial vertex.

Note that if you pass an edge several times, you need to count it into the answer several times.

'''

from typing import List
import collections

class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        # 1. build graph
        # 2. delete leaf nodes with no coins using topological sort
        # 3. delete leaf nodes with coins using topological sort twice
        # 4. count edges * 2

        n = len(coins)
        g = [[] * n for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        indegree = list(map(len, g))
        left_edges = n - 1
        
        # topological sort to delete leaf nodes with no coins
        q = collections.deque()
        for i in range(n):
            if len(g[i]) == 1 and coins[i] == 0:
                q.append(i)
        
        while q:
            left_edges -= 1
            u = q.popleft()
            for v in g[u]:
                indegree[v] -= 1
                g[v].remove(u)
                if len(g[v]) == 1 and coins[v] == 0:
                    q.append(v)

        # topological sort to delete leaf nodes with coins
        for i in range(n):
            if len(g[i]) == 1 and coins[i] == 1:
                q.append(i)
        
        while q:
            u = q.popleft()
            for v in g[u]:
                g[v].remove(u)
                if len(g[v]) == 1 and coins[v] == 1:
                    q.append(v)
        left_edges -= len(q)

        # count edges
        for u in q:
            for v in g[u]:
                indegree[v] -= 1
                if indegree[v] == 1:
                    left_edges -= 1
        
        return max(0, left_edges * 2)