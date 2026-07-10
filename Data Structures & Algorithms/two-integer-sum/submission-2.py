# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         summedIndexes = []
#         if len(nums) < 1:
#             return summedIndexes
#         diff_to_index = {}
#         for i in range(0, len(nums)):
#             num = nums[i]
#             diff = target - num
#             if num in diff_to_index:
#                 summedIndexes.append(diff_to_index[num])
#                 summedIndexes.append(i)
#                 return summedIndexes
#             diff_to_index[diff] = i

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        summedIndexes = []
        if len(nums) < 1:
            return summedIndexes
        val_to_index = {}
        for i in range(0, len(nums)):
            num = nums[i]
            diff = target - num
            if diff in val_to_index:
                summedIndexes.append(val_to_index[diff])
                summedIndexes.append(i)
                return summedIndexes
            val_to_index[num] = i

