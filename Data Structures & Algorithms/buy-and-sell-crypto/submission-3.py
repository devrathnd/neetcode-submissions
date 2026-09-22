class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minbuy = prices[0]
        maxp = 0

        for index, sellprice in enumerate(prices):
            maxp = max(maxp, sellprice - minbuy)
            if sellprice < minbuy:
                minbuy = prices[index]

        return maxp