class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)

        # Add original indices
        tasks = [(e, p, i) for i, (e, p) in enumerate(tasks)]
        tasks.sort()

        heap = []
        res = []

        time = 0
        i = 0

        while i < n or heap:

            # If CPU idle, jump to next enqueue time
            if not heap and time < tasks[i][0]:
                time = tasks[i][0]

            # Add all available tasks
            while i < n and tasks[i][0] <= time:
                e, p, idx = tasks[i]
                heappush(heap, (p, idx))
                i += 1

            # Process shortest task
            p, idx = heappop(heap)
            time += p
            res.append(idx)

        return res