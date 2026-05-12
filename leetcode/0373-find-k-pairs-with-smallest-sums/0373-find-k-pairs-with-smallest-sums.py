class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    
        result = []
        heap = []
        

        for i in range(min(len(nums1), k)):
            heappush(heap, (nums1[i] + nums2[0], i, 0))
        
        while heap and len(result) < k:
            curr_sum, i, j = heappop(heap)
            result.append([nums1[i], nums2[j]])
            
            if j + 1 < len(nums2):
                heappush(heap, (nums1[i] + nums2[j+1], i, j+1))
                
        return result