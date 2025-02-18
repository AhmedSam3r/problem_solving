from typing import List


class Solution:
    """
    notes:
        - You must write a solution in O(log(m * n)) time complexity.
        -
    """
    def searchMatrix_linear(self, matrix: List[List[int]], target: int) -> bool:
        """
        time complexity: O(m x log(n))
        notes:
            - we go through each row and then move to the next one,
                so in worst case we visit each row if target is in the last row
            - we traverse rows linearly, can we do better by traversing them logarithmatically ?
            - beats 100% in run time
            - 
        """
        def binary_search(list, target):
            left, right = 0, len(list) - 1
            while left <= right:
                mid = (left + right) // 2
                if list[mid] == target:
                    return True
                elif target > list[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            return False

        for lst in matrix:
            if not (lst[0] <= target <= lst[-1]):
                continue
            res = binary_search(lst, target)
            return res

        return False

    def searchMatrix_logarithmatic(self, matrix: List[List[int]], target: int) -> bool:
        """
        time complexity O(log(n x m))
        space complexity O(1)
        notes:
            - time complexity is total number of elements to traverse which is n*m
            - treat the 2d matrix as a one 1d and perform binary search on it
            - using greg solution `https://www.youtube.com/watch?v=x-dYOtIudzc`
            - the trick is how to locate the index [i][j] given mid, len(matrix), len(matrix[0])
                - i haven't thought enough of this equation
        """
        m = len(matrix)  # row_count
        n = len(matrix[0])  # column_count
        right = (m * n) - 1
        left = 0
        print(matrix)
        while left <= right:
            mid = (left + right) // 2
            i, j = (mid // n), (mid % n)
            mid_num = matrix[i][j]
            print(f"left={left}, right={right}, mid={mid}, current[{i}][{j}]={mid_num}, ")
            if target == mid_num:
                return True
            elif target > mid_num:
                left = mid + 1
            else:
                right = mid - 1

        return False

    def searchMatrix_top_bottom(self, matrix, target):
        """
         time complexity O(log(n)+log(m)) = O(log(n x m))
        space complexity O(1)
        """
        def binary_search(list, target):
            left, right = 0, len(list) - 1
            while left <= right:
                mid = (left + right) // 2
                if list[mid] == target:
                    return True
                elif target > list[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            return False

        if not matrix or not matrix[0]:
            return False

        ROWS_COUNT, COL_COUNT = len(matrix), len(matrix[0])

        # traverse rows in a logarithmatic time to find the target row
        top, bottom = 0, ROWS_COUNT - 1
        while top <= bottom:
            mid_row = top + (bottom - top) // 2
            if matrix[mid_row][0] <= target <= matrix[mid_row][COL_COUNT - 1]:
                break
            elif target < matrix[mid_row][0]:
                bottom = mid_row - 1  # shift up if target less than current row
            else:
                top = mid_row + 1  # shift down if target greater than current row

        # if the top exceeded the bottom top=4, bottom=3
        # that means we couldnot find a valid element
        # that means we searched in all possible rows
        print(f"top={top}, bottom={bottom}, matrix", matrix)
        if top > bottom:
            return False

        # traverse the list in a logarithmatic time to find the target value
        return binary_search(matrix[mid_row], target)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        time complexity O(m x log(n))
        """
        return self.searchMatrix_logarithmatic(matrix, target)



matrix = [[1,3,5,7],
          [10,11,16,20],
          [23,30,34,60]]
target = 34
res = Solution().searchMatrix(matrix, target)
assert res is True

print('--------------------------------------------------')
matrix = [[1,3,5,7],
          [10,11,16,20],
          [23,30,34,60]]
target = 13
res = Solution().searchMatrix(matrix, target)
assert res is False

print('--------------------------------------------------')
matrix = [[1]]
target = 0
res = Solution().searchMatrix(matrix, target)
assert res is False

print('--------------------------------------------------')
matrix = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
target = 6  # achives top>bottom is True
res = Solution().searchMatrix(matrix, target)
assert res is False


print('--------------------------------------------------')
matrix = [[1]]
target = 0
res = Solution().searchMatrix(matrix, target)
assert res is False

print('--------------------------------------------------')
matrix = [[1,3]]
target = 3
res = Solution().searchMatrix(matrix, target)
assert res is True


print('--------------------------------------------------')
matrix = [[1,2,3,4]]
target = 3
res = Solution().searchMatrix(matrix, target)
assert res is True