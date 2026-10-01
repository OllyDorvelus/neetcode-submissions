class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_to_index_map = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in value_to_index_map:
                return [value_to_index_map[diff], i]
            value_to_index_map[num] = i
        return []

            