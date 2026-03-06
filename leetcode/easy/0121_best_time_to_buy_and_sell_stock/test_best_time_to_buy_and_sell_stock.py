import pytest
from .solution import Solution

@pytest.fixture(scope = "module")
def solution():
    return Solution()

class TestBestTimeToBuyAndSellStock_HappyPath:

    @pytest.mark.parametrize("input_prices, expected_profit",
    [
        ([7,1,5,3,6,4], 5),
        ([7,6,4,3,1], 0),
        ([6500,1200,5800,3200,7500,2100,6800,4500,7200,3800], 6300),
        ([
            95, 92, 88, 90, 85, 87, 82, 84, 80, 78,  # Day 1-10
            82, 75, 77, 73, 76, 70, 72, 68, 71, 65,  # Day 11-20
            69, 63, 67, 61, 64, 58, 62, 56, 60, 54,  # Day 21-30
            58, 52, 56, 50, 55, 53, 57, 51, 56, 50,  # Day 31-40
            54, 52, 55, 53, 56, 54, 57, 55, 58, 56,  # Day 41-50 
        ], 8),
        ([1,2,3,4,5,6,7,8,9,10], 9),
    ], ids=[
        "LeetCode 121 Example 1: [7,1,5,3,6,4], Buy in 1 and sell at 6 -> Profit = 5.",
        "LeetCode 121 Example 2: [7,6,4,3,1], No trascation -> Profit = 0.",
        "Test for the medium level numbers: [6500,1200,5800,3200,7500,2100,6800,4500,7200,3800], buy in 1200 and sell on 7500, Profit = 6300",
        "Test for the medium level prices list length: 50 days list, buy in 50, and sell on 58. (Or other pairs).",
        "Test on a day-growing list: [1,2,3,4,5,6,7,8,9,10], Buy in 1 and sell on 10, Profit = 9.",
    ])

    def test_happy_path(self, solution: Solution, input_prices: list[int], expected_profit: int):
        profit = solution.maxProfit(input_prices)
        assert profit == expected_profit

class TestBestTimeToBuyAndSellStock_EdgeCases:

    @pytest.mark.parametrize("input_prices, expected_profit",
    [
        ([100], 0),
        ([0, 5, 0, 10, 0], 10),
        ([10000, 5000, 8000, 3000, 10000], 7000),
        ([x % 100 for x in range(10**5)], 99),
        ([50, 50, 50, 50, 50], 0),
        ([0, 0, 0, 0, 0], 0),
        ([10000]*5, 0),
    ], ids = [
        "Test for the min length.",
        "Test when the min value (0) in the prices list: [0, 5, 0, 10, 0], buy in 5 and sell on 10 -> Profit = 10.",
        "Test when the max value (10000) in the prices list: [10000, 5000, 8000, 3000, 10000], buy in 3000 and sell on 10000 -> Profit = 7000.",
        "Test the max length of prices: [0~99 repeated for 10**4 times], buy in 0 and sell on 99 -> Profit = 99",
        "Test the prices contains all repeated values: [50,50,...50] -> Profit = 0, no transcation.",
        "Test the prices contains all 0: [0,0,0,0,0] -> Profit = 0.",
        "Test the prices contains all 0: [10000]*5 -> Profit = 0.",
    ])

    def test_happy_path(self, solution: Solution, input_prices: list[int], expected_profit: int):
        profit = solution.maxProfit(input_prices)
        assert profit == expected_profit