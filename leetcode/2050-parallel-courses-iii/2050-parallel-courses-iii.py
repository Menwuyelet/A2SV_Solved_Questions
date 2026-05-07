class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        qeue = deque()
        ans = 0
        dist = defaultdict(int)
        for r in relations:
            graph[r[0]].append(r[1])
            in_degree[r[1]] += 1
        
        for i in range(1, n+1):
            if i not in in_degree:
                
                qeue.append(i)
            dist[i] = time[i-1]

        while qeue:
            course = qeue.popleft()
            # order.append(course)

            for neighbor in graph[course]:
                # Current node is removed, so neighbor
                # has one less incoming edge.
                dist[neighbor] = max(dist[neighbor], dist[course] + time[neighbor - 1])
                in_degree[neighbor] -= 1
        
                # If neighbor has no remaining incoming
                # edges, it can now be processed.
                if in_degree[neighbor] == 0:
                    qeue.append(neighbor)
        
    
        return max(dist.values())
