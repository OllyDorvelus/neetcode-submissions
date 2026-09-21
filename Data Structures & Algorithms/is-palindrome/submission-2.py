class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_s = s.lower()
        print(lower_s)
        high_index = len(s) - 1
        low_index = 0

        while low_index < high_index:
            left_char = lower_s[low_index]
            right_char = lower_s[high_index]
            if not left_char.isalnum():
                low_index += 1
                continue
            if not right_char.isalnum():
                high_index -= 1
                continue
            if lower_s[low_index] != lower_s[high_index]:
                return False
            low_index += 1
            high_index -= 1

        
        return True