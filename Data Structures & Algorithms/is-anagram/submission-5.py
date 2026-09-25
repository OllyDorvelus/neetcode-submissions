from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq_s_map = defaultdict(int)
        freq_t_map = defaultdict(int)

        for char in s:
            freq_s_map[char] += 1
        
        for char in t:
            freq_t_map[char] += 1
        
        for key in freq_s_map:
            if freq_s_map.get(key, -1) != freq_t_map.get(key, 0):
                return False
        return True 
        