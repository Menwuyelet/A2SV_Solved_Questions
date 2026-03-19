class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjecency_list = defaultdict(list)

        for edge in edges:
            adjecency_list[edge[1]].append(edge[0])
            adjecency_list[edge[0]].append(edge[1])

            
        visited = set()
        def dfs(node):
            if node == destination:
                return True
            
            visited.add(node)
            for neighbour in adjecency_list[node]:
                if neighbour not in visited:
                    if dfs(neighbour):
                        return True
            return False
        
        return dfs(source)