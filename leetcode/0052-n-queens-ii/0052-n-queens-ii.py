class Solution:
    def totalNQueens(self, n: int) -> int:
                # we track the variables we need for the decisision making
        col = set()
        positive_diagonal = set()
        negative_diagonal = set()

        ans = 0
        board = [(["."] * n) for i in range(n)]
        
        def backtrack(row):
            nonlocal ans
            # if we are at the last row we add the solution to our ans and return to try other ways
            if row == n:

                # we compy the board and convert its rows to string since that is what we are asked to giveback
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