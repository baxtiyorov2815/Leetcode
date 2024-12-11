class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy_price = prices[0]
        profit = 0

        for i in prices[1:]:
            if i < buy_price:
                buy_price = i

            profit = max(profit, i - buy_price)

        return profit


test = Solution()
print(test.maxProfit([7,1,5,3,6,4]))