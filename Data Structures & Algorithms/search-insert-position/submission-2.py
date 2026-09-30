class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low_index = 0
        high_index = len(nums) - 1
        mid_index = (high_index + low_index) // 2

        if target < nums[low_index]:
            return 0

        while low_index <= high_index:
            if target > nums[mid_index]:
                low_index = mid_index + 1
            elif target < nums[mid_index]:
                high_index = mid_index - 1
            else:
                return mid_index
            mid_index = (high_index + low_index) // 2
     #   print("mid", mid_index)
        return mid_index + 1 if target > nums[mid_index] else mid_index