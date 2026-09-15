class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s, count_t = {}, {}

        for char in s:
            if char in count_s:
                count_s[char] += 1
            else:
                count_s[char] = 1

        for char in t:
            if char in count_t:
                count_t[char] += 1
            else:
                count_t[char] = 1

        for char_key in count_s:
            if char_key not in count_t or count_s[char_key] != count_t[char_key]:
                return False
        return True