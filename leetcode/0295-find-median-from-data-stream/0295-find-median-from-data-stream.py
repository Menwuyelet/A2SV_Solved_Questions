"""
- The question: we are tasked to implement a find median class that finds a median of a data stream.
- Solution:
    - to find a median there is two scenarios, 
            1, the length of the data stream is odd so the median is the number in the midle fo the datastream
            2, the length of the data stream is even, this time there is no one median we calculate it by using the two elements in the midle we add them and devide them to two.
    - so in our class we should also consider these two scenarios as well as tracking the midle.
    - the bruteforce way is to calculate storing the data stream in a list and for each query calculate the median and return it.
    - but this is costy.
    - instead we can use two heaps, one heap_max and one heap_min 
    - since the data stream is not sorted we can use the two heaps to store the data separated in two sides and sort it, one storing the upper side(above the median value) using heap_min and the other to store the side below the median value usin heap_max so both the top elements are going to be max of the smaller half and min of the upper half.
    - by doing this we garantee to always get the two posible median values(or the two used to calculate it) at the top or our two heaps.
    - to accomodate the two cases and to know to which we add the newly incoming value to maintain the median property we check the length of the two heaps we follow a sequence of steps.
        1, we imidietly add the newly added number to the heap that contains the bellow side 
        2, we check if the larger element of the smaller half is larger than the smallest element in the upper half, if so we pop the larger element from the smaller half and add it to the upper half
        3, if the length of the heap containing the down half is larger than the length of the heap containing the upper half + 1 we pop from the small half and add it to the larger half.
        else we leave it there.
    - by following the above steps we maintain the median structure, now when query is processed we check 3 scenarios.
            1, the down half heap is larger than the upper half, if so we take the top of the down half heap as our median
            2, if the down half heap is smaller than the upper half, we take the top of the upper half as our median
            3, else we take both top elements from the two heaps and calculate the median.
    - and that is it.
-  Time and Space complexity:
    - Time = O(log n) - to add new data, O(1) to find the median, n = len(data stream)
    - space = O(n), 
"""

class MedianFinder:
    def __init__(self):
        self.small = []   
        self.large = []   

    def addNum(self, num: int) -> None:

        # we add the new data to the down half 
        heappush_max(self.small, num) 

        # we check if the max value of the down half is larger than the min value of the upper half, if so we move it to the upper half
        if self.large and self.small[0] > self.large[0]:
            val = heappop_max(self.small)
            heappush(self.large, val)

        # if the len of the down half is larger than the len of the upper half by more than 1 we take one element from the down half and move it to the upper half.
        if len(self.small) > len(self.large) + 1:
            heappush(self.large, heappop_max(self.small))

        # if the len of the upper half is larger than the buttom half we take one element from the upper and add it to the buttom
        if len(self.large) > len(self.small) + 1:
            heappush_max(self.small, heappop(self.large))

    def findMedian(self) -> float:

        # if the down half is larger than the upper half the median is in the down half and it is the max element
        if len(self.small) > len(self.large):
            return self.small[0]

        # if the upper half is larger then the median is in the upper half and it is the min element
        if len(self.large) > len(self.small):
            return self.large[0]

        # else if both are the same size the size of the data stream is even so we take one element from both halfs and calculate the median
        return (self.small[0] + self.large[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()