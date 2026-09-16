class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_to_index_map: dict[int,int] = {}
        for i in range(0, len(nums)):
            num = nums[i]
           #if num not in val_to_index_map:
            val_to_index_map[num] = i
        print("map", val_to_index_map)
        
        for i in range(0, len(nums)):
            num = nums[i]
            val_to_find = target - num
            if val_to_find in val_to_index_map and i != val_to_index_map[val_to_find]:
                return sorted([i, val_to_index_map[val_to_find]])