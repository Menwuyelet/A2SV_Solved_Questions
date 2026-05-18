class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empty_cells.append((r, c))
                else:
                    num = board[r][c]
                    rows[r].add(num)
                    cols[c].add(num)

                    box_index = (r // 3) * 3 + (c // 3)
                    boxes[box_index].add(num)

        def backtrack(index):

            if index == len(empty_cells):
                return True

            r, c = empty_cells[index]
            box_index = (r // 3) * 3 + (c // 3)

            for num in "123456789":

                if (
                    num not in rows[r]
                    and num not in cols[c]
                    and num not in boxes[box_index]
                ):

                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box_index].add(num)

                    if backtrack(index + 1):
                        return True

                    board[r][c] = "."
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[box_index].remove(num)

            return False

        backtrack(0)