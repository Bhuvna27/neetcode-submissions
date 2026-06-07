class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        b, s = 0,1
        max_profit = 0
        while s < len(prices):
            if prices[s] > prices[b]:
                profit = prices[s] - prices[b]
                max_profit = max(profit, max_profit)
            else:
                b = s
            s += 1
        return max_profit

                




            


        

        