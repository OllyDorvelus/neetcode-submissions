class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_index = 0
        right_index = len(nums) - 1
        mid_index = right_index // 2

        while left_index <= right_index:
            if target < nums[mid_index]:
                right_index = mid_index - 1
            elif target > nums[mid_index]:
                left_index = mid_index + 1
            else:
                return mid_index
            mid_index = (right_index + left_index) // 2

        return -1