from typing import List
from collections import defaultdict


class Solution:
    """
    Time Complexity:
        The time complexity of the solution is O(N) and space complexity O(N)
        The board size is fixed at 9x9, giving N=81.
        The algorithm iterates over each cell exactly once using a nested loop:
        Outer loop iterates over rows (9 iterations).
        Inner loop iterates over columns (9 iterations).
        For each cell, constant-time operations are performed: checking membership in sets and adding elements to sets.
        Thus, the overall time complexity is O(NxN), O(9×9)=O(81)=O(N),
        but since  N is constant (81), the complexity is effectively
        O(1) in practical terms.

    Space Complexity:
        The space complexity is also 
        O(NxN), which translates to O(1)
        O(1) given the fixed size of the Sudoku board.

        Space for Rows, Columns, and Squares Sets:
        Three dictionaries (rows, cols, squares) are used to store sets.
        Each dictionary can hold up to 9 keys, one for each row, column, or square.
        Each set within the dictionaries can hold up to 9 elements (digits 1-9), but only filled cells contribute.
        Maximum Elements Stored:
        In the worst case, all cells are filled, requiring storage for 81 elements spread across these sets.
        Given the constant board size, the space required remains bounded, making the space complexity 
        O(1) in practice.
    """
    def sub_sudoko(self, board, row_start, col_start):
        length = 3
        nums = set()
        for row in range(row_start, row_start + length):
            for col in range(col_start, col_start + length):
                num = board[row][col]  # can we sitch [col][row] to check column in one pass ? I guess yes
                print("NUM ==>", num, end=' ')
                if num != "." and num in nums:
                    print(f"IN ROW [{row}][{col}] & num={num}" )
                    return False
                nums.add(num)
            print("new")
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        time complexity:
            O(n^2) + O(m^2) where m=3 = O(n^2) since n is constant 
            therefore O(N)
        space complexity:
            O(n)
        notes:
            my solution is simpler and don't overuse memory
            but the other solution is smarter in terms of visualizations and
            mapping visualizations into an implementation

        """
        length = 9
        for row in range(length):
            row_set = set()
            col_set = set()
            for col in range(length):
                num_row = board[row][col]  # can we sitch [col][row] to check column in one pass ? I guess yes
                num_col = board[col][row] 
                if num_row != "." and num_row in row_set:
                    print(f"IN ROW [{row}][{col}] & num={num_row}" )
                    return False
                if num_col != "." and num_col in col_set:
                    print(f"IN COL [{col}][{row}] & num={num_row}" )
                    return False
                row_set.add(num_row)
                col_set.add(num_col)

        # for row in range(length):
        #     for col in range(length):
        #         if (row % 3 == 0 and col % 3 == 0):
        #             print("ROW ==>", row, "COL ==>", col, (row % 3 == 0 and col % 3 == 0))
        #             if self.sub_sudoko(board, row, col) is False:
        #                 return False
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                if not self.sub_sudoko(board, row, col):
                    return False
        return True

    def is_valid_sudoku_boxes_solution(self, board):
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)  # square is a 3x3
        for row in range(9):
            for col in range(9):
                current = board[row][col]
                if current == ".":
                    continue
                # this equations ensures that the row or column lies in one of the 3*3 grid
                row_box_index, col_box_index = row//3, col//3
                if (
                    current in rows[row] or
                    current in cols[col] or
                    current in squares[(row_box_index, col_box_index)]
                ):
                    return False

                rows[row].add(current) # this way we iterate over rows by rows[rowNumber]
                cols[col].add(current)  # this way we iterate over cols by cols[ColumnNumber]
                squares[(row_box_index, col_box_index)].add(current)
            print("squares", squares)
            print('-------------')
            print("rows ", rows[2])
            print('-------------')
            print("rows ", cols)
            return True


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
# res = Solution().isValidSudoku(board)
# print("RES ===>", res)
res = Solution().is_valid_sudoku_boxes_solution(board)
print("RES ===>", res)


board = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
# res = Solution().isValidSudoku(board)
# print("RES ===>", res)
