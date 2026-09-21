class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_to_index_map: dict[int,int] = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in val_to_index_map:
                return [val_to_index_map[diff], i]
            val_to_index_map[n] = i
        # for i in range(0, len(nums)):
        #     num = nums[i]
        #     val_to_index_map[num] = i
        
        # for i in range(0, len(nums)):
        #     num = nums[i]
        #     val_to_find = target - num
        #     if val_to_find in val_to_index_map and i != val_to_index_map[val_to_find]:
        #         return [i, val_to_index_map[val_to_find]]
        return []