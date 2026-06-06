class Solution:
    def getSkyline(self, buildings):

        # create events
        events = []

        for left, right, height in buildings:
            events.append((left, -height, right))
            events.append((right, 0, 0))

        events.sort()

        # max heap
        heap = [(0, float('inf'))]

        result = []
        prev_height = 0

        for x, neg_h, right in events:

            # remove expired buildings
            while heap and heap[0][1] <= x:
                heappop(heap)

            # add new building
            if neg_h:
                heappush(heap, (neg_h, right))

            # current max height
            current_height = -heap[0][0]

            # skyline changed
            if current_height != prev_height:
                result.append([x, current_height])
                prev_height = current_height

        return result