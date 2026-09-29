class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximumValue = 0
        for i in range(len(prices)):
            buyingPrice = prices[i]
            for j in range(len(prices)-1, i, -1):
                sellingPrice = prices[j]
                profit = sellingPrice - buyingPrice
                if profit > maximumValue:
                    maximumValue = profit
        if maximumValue > 0:
            return maximumValue
        else:
            return 0

                
        
        