class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        left_pointer = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[left_pointer], nums[i] = nums[i], nums[left_pointer]
                left_pointer += 1
        return left_pointer