"""
- The question: given two list of integers we are tasked to return the intersection of the two lists.
- Solution:
    - we can solve this problem using set. 
    - converting the lists to set and performing the intersection opration on the two sets.
-  Time and Space complexity:
    - Time = O(n+m), n = len(nums1), len(nums2)
    - space = O(n+m)
"""
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set_nums1 = set(nums1)
        set_nums2 = set(nums2)
        ans = set()

        ans = set_nums1.intersection(set_nums2)

        answer = list(ans)
        return answer
            