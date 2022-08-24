class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # look for the index of the lowest value
        # look for the max value with an index greater than that of the lowest value
        # return the difference
        curr_diff = max_diff = 0
        i = 0
        j = 1
        while (j < len(prices)):
            curr_diff = prices[j] - prices[i]
            if prices[j] < prices[i]:
                i = j
            else:
                max_diff = max(curr_diff, max_diff)
            j += 1
        return max_diff