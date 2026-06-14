import heapq
from typing import List

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        if len(target) == 1:
            return target[0] == 1

        total = sum(target)

        # max heap using negatives
        heap = [-x for x in target]
        heapq.heapify(heap)

        while True:
            largest = -heapq.heappop(heap)
            rest = total - largest

            # valid ending condition
            if largest == 1 or rest == 1:
                return True

            # impossible cases
            if rest == 0 or largest < rest or largest % rest == 0:
                return False

            prev = largest % rest

            total = rest + prev
            heapq.heappush(heap, -prev)