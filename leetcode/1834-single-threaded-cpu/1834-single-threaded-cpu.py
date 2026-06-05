"""
- The question: we are given a list of tasks in a 2d array each task containing its starting time and the duration of time it takes to be processed. we also have a single threaded cpu that process the tasks. and we are tasked to return the list of the tasks based on the processing order.
- Solution:
    - this problem seems so simple at first glance, but when we look close we see that it has several constraints hiding.
    - to start of we need to sort the tasks as they are not given to us sorted,
    - second, when we go to the next time we don't only process one task, but we take all the tasks that start at that time and we process them based on theire processing time.
    - third we need to iterate until both we reached last task and there are no available tasks to be processed, else we continue to proccess them.
    - so to implement this ificiently we need to know which task is the first to be processed in each iteration, this is determind by starting time(availablity) or if there are multiple available tasks by theire time to be processed.
    - to achive this instant geting of the next task we use heap.
    - so we iterate over the tasks and we add all currently available tasks to our heap.
    - after we finish that we pop the top of the heap and add its time to our cpu time to occupy that time and add the task index to our ans, we do taht until we reach end of the task and our heap is empty.
    - and that is it.
-  Time and Space complexity:
    - Time = O(n log n), n = len(tasks)
    - space = O(n), 
"""

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)

        # pack the tasks with theire original index before sorting
        tasks = [(e, p, i) for i, (e, p) in enumerate(tasks)]
        tasks.sort()

        heap = []
        res = []

        time = 0
        i = 0

        # we iterate until we both reach end of tasks and our heap is empty
        while i < n or heap:

            # if CPU is idle, jump to next tasks enqueue time directly
            if not heap and time < tasks[i][0]:
                time = tasks[i][0]

            # we add all currently posible tasks to our heap so we can take the correct one to be processed at this time
            while i < n and tasks[i][0] <= time:
                e, p, idx = tasks[i]
                heappush(heap, (p, idx))
                i += 1

            # we take the shortest task from our all available tasks in the heap
            p, idx = heappop(heap)
            time += p
            res.append(idx)

        return res