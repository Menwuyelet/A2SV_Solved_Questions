class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        merged = []
        i, j = 0, 0

        # merge step 
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        
        # add remaining elements
        merged.extend(nums1[i:])
        merged.extend(nums2[j:])

        n = len(merged)

        # find median
        if n % 2 == 1:
            return merged[n // 2]
        else:
            return (merged[n // 2 - 1] + merged[n // 2]) / 2