"""
- The question: we are given n * m matrix and target, we are tasked to see if the target exists in the given matrix, if so return True else False
- Solution:
    - so we could just use linear search to solve this problem but it will be n * m time. but we are tasked to solve it in log(n * m)
    - so we use binary search to solve it.
    - first we should find in which row the target will be if it exists and after we find the row we do another binary search on that row(normal list binary search) to see if the target exists or not.
    - if so we return True else False.
-  Time and Space complexity:
    - Time = O(log n * m), n = len(nums)
    - space = O(1), 
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # we first check if there exist a row that could contain the given target if the target is present in the matrix.
        row = find_row(matrix, target)

        # if there is no row that contains the target we return False 
        if row == -1:
            return False

        # else there is a potential row that is containing the targate we do binary search on it and check if the target is present or not.
        else:
            
            # we use a helper function to do the binary search on the row
            ans = find_ans(matrix[row], target)

            if ans == -1:
                return False
            else:
                return True



# this helper function is used to determine the row that could conatin the target
def find_row(matrix, target):
    top, bottom = 0, len(matrix) - 1

    while top <= bottom:
        mid = (top + bottom) // 2

        if target > matrix[mid][-1]:
            top = mid + 1
        elif target < matrix[mid][0]:
            bottom = mid - 1
        else:

            # if the row exist we return its index
            return mid

    # else -1
    return -1


# after we find the rwo we do another binary search on that row to check if the row contains the target or not.
def find_ans(row, target):
    left, right = 0, len(row) - 1

    while left <= right:
        mid = (left + right) // 2

        if target > row[mid]:
            left = mid + 1
        elif target < row[mid]:
            right = mid - 1
        else:

            # if the target exist we return its index
            return mid

    # else -1
    return -1