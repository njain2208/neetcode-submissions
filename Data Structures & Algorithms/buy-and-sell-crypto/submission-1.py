class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minStockPrice, maxStockPrice = float("inf"), 0
        
        for i in range(len(prices)):
            minStockPrice  = min(prices[i], minStockPrice)

            maxStockPrice = max(maxStockPrice, prices[i] - minStockPrice)
        
        return maxStockPrice
        