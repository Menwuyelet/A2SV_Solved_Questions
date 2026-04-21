"""
- The question: we are given an n by n chessboard and n queens. and we are tasked to the number of distict arrangements so that no queen attacks the others.
- Solution:
    - so to solve this problem we use bruteforce backtracking.
    - but first we need to define some base rules. 
            1. no queens can be on the same row
            2, no queens can be on the same column
            3, no queens can be on the same diagonal (positive or negative)
        
    - the above 3 rules are the bases to solve this problem.
    - what we do is iterate over all the rows and check if one of the above conditions will be violated if we put a queen on the current row, column.
    - if so we jump the column and continue to the next column on the same row, else we add queen to that cell and track it for future comparations.
    - after that we try the remaining possible placments by backtracking.
    - we use three variables to track visited columns, positive diagonals and negative diagonals. the row is auto tracked by the given input.
    - we track the diagonals by row + column for positive and row - column for negative
    - and that is it.
-  Time and Space complexity:
    - Time = O(n!), n = n,  k = total posible solutions
    - space = O(k⋅n2) 
"""
class Solution:
    def totalNQueens(self, n: int) -> int:
                # we track the variables we need for the decisision making
        col = set()
        positive_diagonal = set()
        negative_diagonal = set()

        ans = 0
        board = [(["."] * n) for i in range(n)]
        
        def backtrack(row):

            # we should declare nonlocal to access the global var in backtracking
            nonlocal ans

            # if we are at the last row we add the solution to our ans and return to try other ways
            if row == n:

                # we increase our ans by 1 as we found 1 posible answer
                ans += 1
                return 
            

            for colmn in range(n):

                # if one of the above rules will be violated if we put queen on the current cell we jump it
                if colmn in col or (colmn + row) in positive_diagonal or (row - colmn) in negative_diagonal:
                    continue
                
                # else we track the current cell for next comparations and add queen to it
                col.add(colmn)
                positive_diagonal.add(colmn + row)
                negative_diagonal.add(row - colmn)

                board[row][colmn] = "Q"

                # we continue to the next row to compleet the board
                backtrack(row + 1)

                # we clean up the record to try other possible ways backtraking
                col.remove(colmn)
                positive_diagonal.remove(colmn + row)
                negative_diagonal.remove(row - colmn)

                board[row][colmn] = "."

        # we start at the first row
        backtrack(0)
        
        return ans