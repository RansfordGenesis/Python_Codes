class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for x in prices:
            min_price = min(min_price, x)
            max_profit = max(max_profit, x-min_price)
        return max_profit
