class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_pointer = 0
        right_pointer = len(s) - 1
        lower_s = s.lower()
        while left_pointer < right_pointer:
            if not lower_s[left_pointer].isalnum():
                left_pointer += 1
                continue
            if not lower_s[right_pointer].isalnum():
                right_pointer -= 1
                continue
            if lower_s[left_pointer] != lower_s[right_pointer]:
                return False
            left_pointer += 1
            right_pointer -= 1

        return True