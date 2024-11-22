class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        
        # first find the row that the target will be in

        top_row, bottom_row = 0, ROWS - 1
        while top_row < bottom_row:

            # find the middle row
            row = (top_row + bottom_row) // 2

            if target > matrix[row][-1]:
                top_row += 1
            elif target < matrix[row][-1]:
                bottom_row -= 1
            else:
                break

        if top_row > bottom_row:
            return False
        row = (top_row + bottom_row) // 2
        left, right = 0, COLS - 1

        # now we will do another binary search in the selected row
        # from the previous binary search
        while left <= right:
            m = (left + right) // 2
            if matrix[row][m] > target:
                right = m - 1
            elif matrix[row][m] < target:
                left = m + 1
            else:
                return True
        return False