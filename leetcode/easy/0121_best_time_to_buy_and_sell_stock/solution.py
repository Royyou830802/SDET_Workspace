class Solution:
    def CheckInput(self, prices: list[int]):
        if not isinstance(prices, list):
            raise TypeError("The input prices is not a list.")
        if len(prices) > 10**5:
            raise ValueError("The input prices length is too long.")
        if any([not isinstance(x,int) for x in prices]):
            raise TypeError("There is a non-integer value in the prices list.")
        if any([x > 10**4 for x in prices]):
            raise ValueError("The value in the prices list exceed upper bound 10000")
        if any([x < 0 for x in prices]):
            raise ValueError("The value in the prices list exceed lower bound 0")
        
    def maxProfit(self, prices: list[int]) -> int:
        self.CheckInput(prices)
        # Can only buy and sell 1 time
        k = 1
        # Define the state
        s1 = [float("-inf")] * k # s1[i]: The maximum profit at the i time holding the stock
        s2 = [0] * (k + 1) # s2[i]: The maximum profit at the i time selling the stock
        for day in range(len(prices)):
            for i in range(k): 
                # At the i time buying / selling
                s1[i] = max(s2[i] - prices[day], s1[i]) # Max the profit when i time buying
                s2[i + 1] = max(s1[i] + prices[day], s2[i + 1]) # Max the profit when i time selling
        # Max profit is the state after several times selling or do not trading
        profit = max(s2)
        return profit