import pytest
from solution import Solution


@pytest.fixture
def solution():
    return Solution()


class TestTwoSumBasic:
    """基本功能測試"""

    @pytest.mark.parametrize("nums, target, expected", [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([1, 5, 3, 6], 8, [1, 2]),
        ([1, 2, 3, 4], 7, [2, 3]),
    ], ids=[
        "[2,7,11,15] t=9 -> [0,1]",
        "[1,5,3,6] t=8 -> [1,2]",
        "[1,2,3,4] t=7 -> [2,3]",
    ])
    def test_basic(self, solution, nums, target, expected):
        assert solution.twoSum(nums, target) == expected


class TestTwoSumEdgeCases:
    """邊界條件測試"""

    @pytest.mark.parametrize("nums, target, expected", [
        ([3, 3], 6, [0, 1]),
        ([-1, -2, -3, -4], -6, [1, 3]),
        ([0, 4, 3, 0], 0, [0, 3]),
        ([-3, 4, 3, 90], 0, [0, 2]),
        ([1000000000, 2, 999999998], 1000000000, [1, 2]),
    ], ids=[
        "[3,3] t=6 -> [0,1]",
        "[-1,-2,-3,-4] t=-6 -> [1,3]",
        "[0,4,3,0] t=0 -> [0,3]",
        "[-3,4,3,90] t=0 -> [0,2]",
        "[1e9,2,999999998] t=1e9 -> [1,2]",
    ])
    def test_edge_cases(self, solution, nums, target, expected):
        assert solution.twoSum(nums, target) == expected


class TestTwoSumDuplicates:
    """重複元素測試"""

    @pytest.mark.parametrize("nums, target, expected", [
        ([3, 3], 6, [0, 1]),
        ([3, 3, 4], 7, [1, 2]),
    ], ids=[
        "[3,3] t=6 -> [0,1]",
        "[3,3,4] t=7 -> [1,2]",
    ])
    def test_duplicates(self, solution, nums, target, expected):
        assert solution.twoSum(nums, target) == expected


class TestTwoSumReturnValue:
    """回傳值驗證"""

    def test_returns_two_indices(self, solution):
        result = solution.twoSum([2, 7, 11, 15], 9)
        assert len(result) == 2
        assert all(isinstance(i, int) for i in result)

    def test_indices_sum_to_target(self, solution):
        nums = [2, 7, 11, 15]
        target = 9
        result = solution.twoSum(nums, target)
        assert nums[result[0]] + nums[result[1]] == target

    def test_smaller_index_first(self, solution):
        result = solution.twoSum([2, 7, 11, 15], 9)
        assert result[0] < result[1]
