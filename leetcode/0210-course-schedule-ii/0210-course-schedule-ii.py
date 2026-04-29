class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        incoming = [0 for _ in range(numCourses)]
        qeue = deque()
        order = []

        for course, pre in prerequisites:
            graph[pre].append(course)
            incoming[course] += 1

    
        for course in range(numCourses):
            if incoming[course] == 0:
                qeue.append(course)
        

        while qeue:
            course = qeue.popleft()
            order.append(course)

            for neighbour in graph[course]:
                incoming[neighbour] -= 1

                if incoming[neighbour] == 0:
                    qeue.append(neighbour)

        if len(order) != numCourses:
            return []

        return order