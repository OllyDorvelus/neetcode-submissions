# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        high_num = n
        low_num = 1
        
        while low_num <= high_num:
            mid_num = (low_num + high_num) // 2
            target = guess(mid_num)
            if target == -1:
                high_num = mid_num - 1
            elif target == 1:
                low_num = mid_num + 1
            else:
                return mid_num
        return -1