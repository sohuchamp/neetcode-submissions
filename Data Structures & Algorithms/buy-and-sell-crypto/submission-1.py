class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minimumPrice = prices[0]
        maximumProfit = 0
        for i in range(len(prices)):
            
            profit = prices[i] - minimumPrice
            if profit > maximumProfit:
                maximumProfit = profit
            if (prices[i] < minimumPrice):
                minimumPrice = prices[i]
        return maximumProfit
            

                
        
        