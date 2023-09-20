'''
You are given an integer n, which indicates that there are n courses labeled from 1 to n. You are also given an array relations where relations[i] = [prevCoursei, nextCoursei], representing a prerequisite relationship between course prevCoursei and course nextCoursei: course prevCoursei has to be taken before course nextCoursei.

In one semester, you can take any number of courses as long as you have taken all the prerequisites in the previous semester for the courses you are taking.

Return the minimum number of semesters needed to take all courses. If there is no way to take all the courses, return -1.
'''

from typing import List
import collections

class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        indegree = {i: 0 for i in range(1, n + 1)}
        g = collections.defaultdict(list)
        for u, v in relations:
            indegree[v] += 1
            g[u].append(v)
        
        q = collections.deque()
        for i in range(1, n + 1):
            if indegree[i] == 0:
                q.append(i)
        
        ans = 0
        while q:
            size = len(q)
            for _ in range(size):
                u = q.popleft()
                n -= 1
                for v in g[u]:
                    indegree[v] -= 1
                    if indegree[v] == 0:
                        q.append(v)
            ans += 1
        
        return ans if n == 0 else -1



        
