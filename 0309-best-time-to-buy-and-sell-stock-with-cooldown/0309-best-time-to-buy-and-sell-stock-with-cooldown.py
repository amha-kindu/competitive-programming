class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    sell = 0
    hold = -float('inf')
    prev = 0

    # Loop through each price in the prices array
    for price in prices:
      cache = sell
      sell = max(sell, hold + price)
      hold = max(hold, prev - price)
      # Update the previous sell value to be the cached sell value from the beginning 
      # of the iteration
      prev = cache

    return sell