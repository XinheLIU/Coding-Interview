class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not len(prices):
            return 0
        price_diff = [x - y for x,y in zip(prices[1:], prices[:-1])]
        pos_diff = filter(lambda x: x > 0, price_diff)
        return sum(pos_diff)