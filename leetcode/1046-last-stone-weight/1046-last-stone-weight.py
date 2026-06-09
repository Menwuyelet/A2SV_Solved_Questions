"""
- The question: we are given a list of integers representing weight of stones and tasked to perform a task and return the remaining one stone weight.
                - the task is we take the first two heiviest stones and smash them together, when we do that if they are equal no stone survives else the heaviest stone survive but its weight will be reduced by the weight of the second stone and we put that back to our list.
- Solution:
    - this is fairly easy problem specialy if we are familiar with heap concept.
    - the brute force approach will be that we sort the list take the two largest smash them and put what is remaining back to the list and again sort them and do the same thing untile we are left with only one or none stones.
    - this cost us n * n log n complexity, not very efficient.
    - the solution to this is that we use heap, we use max heap and every time we take the two heaviest stones and smash them and put what is left in the heap and we do that untile we are left with 1 stone or 0.
    - the same approach but the diffrence is that we used heap instead of a list and that gives us log n of inserting and finding the max element at the same time.
    - this would make our solution very efficient.
    - we iterate until we are left with one or zero element and return accordingly. 
    - and that is it
-  Time and Space complexity:
    - Time = O(n log n), n = len(stones)
    - space = 1, 
"""

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapify_max(stones)

        # we iterate until only one element is left
        while len(stones) > 1:
            # we get the first and second max elements
            first = heappop_max(stones)
            second = heappop_max(stones)

            # if they are equal we just continue since none of them survives
            if first == second:
                continue

            # else we push back the remaining surviving stone parts back to our heap
            else:
                heappush_max(stones, first-second)
            

        # if there is stone left we return it
        if stones:
            return stones[0]
        
        # else all are smashed we return 0
        return 0