"""
- The question: we are given a stream of a numerical data and we are tasked to design a class that takes these stream of numerical data and return the kth largest element every time updating the list.
- Solution:
    - the brute force approch would be to add every incoming element in to a list and sort the list every time we add new element.
    - or we could also use binary search to find the exact location of the current element and check if it affects the current kth element.
    - but with out all that complication we coud simply use heap.
    - we hepify our initial list and reduce our heap to contain only k elements and the top element will be the kth element we need.
    - every time we add new element we check if it is larger than the current top element.
    - and if so we pop form our heap and push the current element to the heap this will find the neew kth element.
    - but if it is smaller or equal to our current top element we just ignore that value and return the current top element.
    - and tha is it.
-  Time and Space complexity:
    - Time = O(n log n) - __init__(), O(log n) worst case and O(1) best case for add()
    - space = O(k) for both
"""
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k
        heapify(self.heap)

        # we initialize our list to be heap and contain only k largest elements as kth largest being at the top
        while len(self.heap) > self.k:
            heappop(self.heap)

    def add(self, val: int) -> int:

        # we check if the current value is larger to our kth largest and if so we add it to our heap and pop the current top to find the new kth element
        # but else we just ignore it completly because it wont add any value adding it to our heap
        if self.heap and len(self.heap) >= self.k and val > self.heap[0]:

            # we push our new val
            heappush(self.heap, val)

            # we pop our curr kth element to find the next kth element
            heappop(self.heap)
        
        # if our heap is empty initialy we just add the curretn value and return the new top
        elif not self.heap or len(self.heap) < self.k:
            heappush(self.heap, val)

        return self.heap[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)