class Solution:
    def search(self, nums: List[int], target: int) -> int:
        high_index = len(nums) - 1
        low_index = 0
        len_nums = len(nums)

        while low_index <= high_index:
            mid_index = (high_index + low_index) // 2
            value_at_mid_index = nums[mid_index]

            if value_at_mid_index == target:
                return mid_index

            if value_at_mid_index < target:
                low_index = mid_index + 1
            elif value_at_mid_index > target:
                high_index = mid_index - 1

        return -1