"""
- The question: we are given two int arrays and an integer k and tasked to return a list of k smallest sum pairs one from each array.
- Solution:
    - to solve this by brute force would be by generating all possible pairings and sorting them and returning k smallest pairs.
    - but this approach requires to process the two arrays to give all the summs and that is so slow.
    - so another idea to solve this is using heap.
    - using heap only wont solve this optimally we also need to find a way we can process the elements up to k length or len of first array for initializing and one pair at a time while keeping smalest pairs.
    - to do that we can first add all the sum of elements up to kth index or all array 1 elements (if k > len(nums1)) with first element of the second array to our heap.
    - affter that we start processing the heap and we pop from the heap and append the pair on our result as it will be the smallest pair in that heap, then we add a pair of number from nums 1 with the same index as the one we poped forom the heap and from nums 2 one index forward to the one we poped from the heap.
    - this guarantees in that first array element the next smallest pair is with the next nums 2 element.
    - we reapeat the process until we hit our k smallest pairs or the heap becomes empty.
    - and that is it.
-  Time and Space complexity:
    - Time = O(k * log(min(len(nums1, k))))
    - space = O(min(len(nums1, k)))
"""

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    
        result = [] 
        heap = []
        

        # we append the sum of all elements or until we find the first k elements in num1 with the first element of num2
        for i in range(min(len(nums1), k)):
            heappush(heap, (nums1[i] + nums2[0], i, 0))
        
        # after adding all first row or until k elements we start processing the heap
        while heap and len(result) < k:
            curr_sum, i, j = heappop(heap)

            # we take the current smallest and append it on our heap
            result.append([nums1[i], nums2[j]])
            
            # after taking the current smallest we move on step with the same num1 element but next num2 element to add it on the heap
            if j + 1 < len(nums2):
                heappush(heap, (nums1[i] + nums2[j+1], i, j+1))
                
        return result