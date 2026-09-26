class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_num = str(x)
        left_pointer = 0
        right_pointer = len(str_num) - 1

        while left_pointer <= right_pointer:
            if str_num[left_pointer] != str_num[right_pointer]:
                return False
            left_pointer += 1
            right_pointer -= 1
        return True