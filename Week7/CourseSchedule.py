from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = defaultdict(list)

        for prereq in prerequisites:
            indegree[prereq[0]] += 1
            adj[prereq[1]].append(prereq[0])

        queue = deque()
        result = []

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            course = queue.popleft()
            result.append(course)

            for adj_course in adj[course]:
                indegree[adj_course] -= 1
                if indegree[adj_course] == 0:
                    queue.append(adj_course)

        return result
