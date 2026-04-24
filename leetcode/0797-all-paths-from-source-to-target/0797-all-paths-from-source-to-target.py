
"""
- The question: we are given a directed and syclic graph and tasked to return all the paths that lead form starting node to the last node.
- Solution:
    - this is simple dfs problem with just backtracking to generate all the paths.
    - so we will write our dfs and add to it a backtracking to track all the paths.
-  Time and Space complexity:
    - Time = O(2^n × n), n = len of longest path
    - space = O(2^n × n), 
"""

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []

        # we will have a dfs that starts at the node and go until it reachs the ending node and track the path.
        def dfs(curr_path, node):

            # when we reach the end path we will append the current path as we completed it.
            if node == len(graph) - 1:
                res.append(curr_path[:])
                return

            # if we did not reach the ending node we will iterate over the neighbour that node have and do dfs.
            for neighbour in graph[node]:
                curr_path.append(neighbour)
                dfs(curr_path, neighbour)

                # we undo our doing for backtracking.
                curr_path.pop()
        
        
        dfs([0], 0)
        return res

