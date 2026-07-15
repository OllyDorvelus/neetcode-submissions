class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        left_pointer = 0
        for right_pointer in range(0, len(nums)):
            if nums[right_pointer] != val:
                nums[left_pointer], nums[right_pointer] = nums[right_pointer], nums[left_pointer]
                left_pointer += 1
        return left_pointer