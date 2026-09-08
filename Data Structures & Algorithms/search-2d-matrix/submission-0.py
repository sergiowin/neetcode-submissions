class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo = 0
        hi = len(matrix) - 1
        while (lo <= hi):
            midRow = lo + ((hi - lo) // 2)
            firstVal = matrix[midRow][0]
            lastVal = matrix[midRow][-1]
            if (target >= firstVal) and (target <= lastVal):
                ##target must be within the row if it is inside the matrix, so now binary search this row
                lo = 0
                hi = len(matrix[midRow]) - 1
                midNum = lo + ((hi - lo) // 2)
                while (lo <= hi):
                    midNum = lo + ((hi - lo) // 2)
                    if matrix[midRow][midNum] == target:
                        return True
                    elif matrix[midRow][midNum] < target:
                        lo = midNum + 1
                    elif matrix[midRow][midNum] > target:
                        hi = midNum - 1
                ## returns false if not found inside this row
                return False
            elif (target < firstVal):
                hi = midRow - 1
            elif (target > lastVal):
                lo = midRow + 1
        ## this should trigger if there is no row that could even potentially contain the target
        return False
        
            