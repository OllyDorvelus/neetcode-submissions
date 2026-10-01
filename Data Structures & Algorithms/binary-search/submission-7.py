class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low_index = 0
        high_index = len(nums) - 1

        while low_index <= high_index:
            mid_index = (low_index + high_index) // 2
            if target > nums[mid_index]:
                low_index = mid_index + 1
            elif target < nums[mid_index]:
                high_index = mid_index - 1
            else:
                return mid_index
        return -1