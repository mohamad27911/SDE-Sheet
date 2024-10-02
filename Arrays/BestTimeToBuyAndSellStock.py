class Solution(object):
    def maxProfit(self, prices):
      max_profit ,min=0,float('inf') 
      for price in prices:
          if price < min:
              min = price
          elif price - min > max_profit:
              max_profit = price-min
      return max_profit
        