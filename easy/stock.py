from typing import List

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=problem-list-v2&envId=array
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for curr_price in prices:
            if curr_price < min_price:
                min_price = curr_price

            running_profit = curr_price - min_price

            max_profit = max(max_profit, running_profit)

        return max_profit
		

solution = Solution()
ans = solution.maxProfit([2,1,2,0,1])

print(ans)
