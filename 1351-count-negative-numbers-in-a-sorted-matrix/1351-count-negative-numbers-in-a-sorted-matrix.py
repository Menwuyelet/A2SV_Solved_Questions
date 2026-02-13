"""
- The question: give 2d array we are tasked to count the number of negative numbers.
- Solution:
    - since our constraints allows it we can use directly traversing the list and count.
    - to make it a litle bit fast we can traverse in reverse since our list is sorted in revers we can find the negative early.
    - if we encounter a positive number we break that nested loop and move to the next iteration in this way we can save a litel time.
    - apart from this approach we have a two pointer approach which eliminates the need to iterate throgh all the rows.
    - we use two pointers one for the row, and another for the column.
    - we start iterating from the butom left. and we check if the number is negative, if so we add that entire row to our count since any number that comes after it is negative. and we reduce the row by 1
    - else if it is positive we add 1 to our column and move to the next element in the row.
    - for the next row since every upper rows will also have positive above a positive we don't need to go back and check. 
-  Time and Space complexity:
    - Time = brute force => O(n * m), two pointers => O(n+m), n = len(grid), m = len(row)
    - space = brute force => O(n + m) due to the slicings to reverse, two pointers => O(1)
"""
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        return two_ptr(grid)


# using Two pointers instead of scanning the whole list
def two_ptr(grid):
    row = len(grid) - 1
    column = 0

    row_len = len(grid[0])

    count = 0
    # starts from bottom left at (row, 0) and iterates by checking and moving up or to right
    while row >= 0 and column < row_len:
        
        # if the current element is negative so as all the elements after it so we skip the row
        if grid[row][column] < 0:
            count += row_len - column
            row -= 1

        # else we move one step to the right and check again
        else:
            column += 1
    
    return count


# iterating through the list and counting the negatives
def brute_force(grid):
    count = 0
    for row in grid[::-1]:
        for num in row[::-1]:
            if num >= 0:
                break
            count += 1
    return count