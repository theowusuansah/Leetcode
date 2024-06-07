class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_num = 0
        min_num = float("inf")

        for price in prices:
            if price < min_num:
                min_num = price
          
            profit = price - min_num

            if profit > max_num:
                max_num = profit

        return max_num
                

                

        