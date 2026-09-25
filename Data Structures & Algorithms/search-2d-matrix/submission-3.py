class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low_row = 0
        high_row = len(matrix) - 1
        
        column_len = len(matrix[0]) - 1

        while low_row <= high_row:
            mid_row = (low_row + high_row) // 2
            if target < matrix[mid_row][0]:
                high_row = mid_row - 1
            elif target > matrix[mid_row][column_len]:
                low_row = mid_row + 1
            else:
                return self.binarySearch(matrix[mid_row], target)
        
        return False


    def binarySearch(self, nums: List[int], target) -> bool:
        low_index = 0
        high_index = len(nums) - 1
        
        while low_index <= high_index:
            mid_index = (low_index + high_index) // 2
            if target > nums[mid_index]:
                low_index = mid_index + 1
            elif target < nums[mid_index]:
                high_index = mid_index - 1
            else:
                return True
        return False