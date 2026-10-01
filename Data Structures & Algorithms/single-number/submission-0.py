from collections import defaultdict

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count_dict = defaultdict(int)

        for num in nums:
            count_dict[num] += 1
        
        for k in count_dict:
            if count_dict[k] == 1:
                return k
        return -1