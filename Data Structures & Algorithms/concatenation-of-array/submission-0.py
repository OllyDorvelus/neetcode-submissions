class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_arr = [None] * (len(nums) * 2)
        new_arr_len = len(new_arr)
        for i in range(0, new_arr_len):
            new_arr[i] = nums[i % len(nums)]
        return new_arr