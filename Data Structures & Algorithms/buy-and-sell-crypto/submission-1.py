class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left_pointer, right_pointer = 0, 1
        maxP = 0
        while right_pointer < len(prices):
            if prices[left_pointer] < prices[right_pointer]:
                maxP = max(maxP, prices[right_pointer] - prices[left_pointer])
            else:
                left_pointer = right_pointer
            right_pointer += 1 

        return maxP