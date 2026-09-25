from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq_s_map = defaultdict(int)
        freq_t_map = defaultdict(int)

        for i in range(0, len(s)):
            freq_s_map[s[i]] += 1
            freq_t_map[t[i]] += 1
        
        for key in freq_s_map:
            if freq_s_map.get(key, -1) != freq_t_map.get(key, 0):
                return False
        return True 
        