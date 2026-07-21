class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        first_word_map: dict[str, int] = {}
        second_word_map: dict[str, int] = {}

        for c in s:
            if c in first_word_map:
                first_word_map[c] += 1
            else:
                first_word_map[c] = 1

        for c in t:
            if c in second_word_map:
                second_word_map[c] += 1
            else:
                second_word_map[c] = 1

        for key in first_word_map:
            if first_word_map[key] != second_word_map.get(key, 0):
                return False
        
        return True