class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        memo = {}
        def max_profit(i=0, bought=False):
            if i == n:
                return 0
            if (i, bought) in memo:
                return memo[(i, bought)]
            
            # Maybe buy the stock
            if not bought:
                memo[(i, bought)] = max( 
                    max_profit(i+1, True)-prices[i],
                    max_profit(i+1, False)
                )
            # Maybe sell the stock
            else:
                memo[(i, bought)] = max(
                    max_profit(i+1, False)+prices[i]-fee,
                    max_profit(i+1, True)
                )
            return memo[(i, bought)]
            
        return max_profit()