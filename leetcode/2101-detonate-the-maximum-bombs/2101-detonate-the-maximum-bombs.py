class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = build_graph(bombs)
        ans = 0

        def dfs(node, visited):
            if node in visited:
                return

            visited.add(node)

            for nei in graph[node]:
                dfs(nei, visited)

        for i in range(len(bombs)):
            visited = set()
            dfs(i, visited)
            ans = max(ans, len(visited))

        return ans


def build_graph(bombs):
    n = len(bombs)
    graph = defaultdict(list)

    for i in range(n):
        x1, y1, r1 = bombs[i]

        for j in range(n):
            if i == j:
                continue

            x2, y2, _ = bombs[j]

            dx = x1 - x2
            dy = y1 - y2

            if dx * dx + dy * dy <= r1 * r1:
                graph[i].append(j)

    return graph