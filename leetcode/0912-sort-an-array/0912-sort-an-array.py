"""
- The question: we are given a list of integers and tasked to sort them.
- Solution:
    - we are tasked to sort the list using an algorithm with time n log n time complexity.
    - there is an algorithm that have the same time complexity, it is merge sort.
    - we will implement merge sort using recursion.
    - we first recursively divide the list in to two parts until we hit a list with len of 1.
    - after that we merge the two divided list parts and in process we sort them using a two pointer on on each lists.
    - we do that recursively.
-  Time and Space complexity:
    - Time = O(n log n), n = len(nums)
    - space = O(n), 
"""

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        # we recursively divide the list in two parts and when we reach our base we start merging again while sortin it
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])

            # after we done spliting it we merge it while also sortin it
            return merge(left, right)

        nums = merge_sort(nums)

        return nums

def merge(left, right):
    res = []
    i = j = 0

    # we merge the splited list in to one back again and we merge it while also sorting it
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    res.extend(left[i:])
    res.extend(right[j:])

    return res