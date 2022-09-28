class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        curr_diff = 0
        max_diff = 0
        length = len(prices)
        
        while sell < length:
            curr_diff = prices[sell] - prices[buy]
            if prices[sell] < prices[buy]:
                buy = sell
            else:
                max_diff = max(curr_diff, max_diff)
            sell +=1
        return max_diff