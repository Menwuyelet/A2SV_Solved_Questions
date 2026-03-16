"""
- The question: we are given a slist of numbers and tasked to perform sorting using the pancake sorting algorithm and return the list of the indexes we fliped the array to perform the sorting.

- Solution:
    - so to solve this we gona choose the maximum element from the unsorted part of the array.
    - after that we flip the array starting from that index to bring it to first of the array. 
    - after that we again flip starting from the end of the unsorted part of the array to put the current max num to its correct posision.
-  Time and Space complexity:
    - Time = O(n^2), n = len(s)
    - space = O(1), Auxiliary
"""
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []

        for size in range(len(arr), 1, -1):

            max_idx = arr.index(max(arr[:size]))

            # we just continue if the current element is in the correct position
            if max_idx == size - 1:
                continue

            # move max to front
            self.flip(max_idx + 1, arr)
            res.append(max_idx + 1)

            # move max to correct position
            self.flip(size, arr)
            res.append(size)

        return res


    def flip(self, k, arr):
        arr[:k] = arr[:k][::-1]