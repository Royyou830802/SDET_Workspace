import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

# @pytest.mark.skip("TODO: add tests")
# def test_example():
#     # Replace with real tests.
#     _ = Solution()
#     pass

class TestRemoveDuplicatesFromSortedArray_HappyPath:
    """基本功能測試"""

    @pytest.mark.parametrize("nums, expected_k, expected_nums", [
        ([1, 1, 2], 2, [1, 2]),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4]),
        ([3,4], 2, [3,4]),
        ([3,4,5,6,7], 5, [3,4,5,6,7]),
        ([1,1,1,1], 1, [1])
    ], ids=[
        "with duplicates 1: [1,1,2] -> k=2, [1,2]",
        "with duplicates 2: [0,0,1,1,1,2,2,3,3,4] -> k=5, [0,1,2,3,4]",
        "without duplicates 1: [3,4] -> k=2, [3,4]",
        "without duplicates 2: [3,4,5,6,7] -> k=5, [3,4,5,6,7]",
        "all same: [1,1,1,1] -> k = 1, [1]"
    ])
    def test_happy_path(self, solution: Solution, nums: list[int], expected_k: int,
                        expected_nums: list[int]):
        k = solution.removeDuplicates(nums)
        assert k == expected_k
        assert nums[:k] == expected_nums

class TestRemoveDuplicatesFromSortedArray_EdgeCases:
    """Test for edge cases"""

    @pytest.mark.parametrize("nums, expected_k, expected_nums",[
        ([11,11,95,95,98,99,99,100,100], 5, [11,95,98,99,100]),
        ([-5,-5,-2,-2,-1,-1,0,1,1,2,5], 7, [-5,-2,-1,0,1,2,5]),
        ([0]*29999, 1, [0]),
        ([57], 1, [57])
    ], ids = [
        "Large values: [11,11,95,95,98,99,99,100,100] -> k = 5, [11,95,98,99,100]",
        "Negative values: [-5,-5,-2,-2,-1,-1,0,1,1,2,5] -> k = 7, [-5,-2,-1,0,1,2,5]",
        "Very long array: zeros(29999) -> k = 1, [0]",
        "Single element: [57] -> k = 1, [57]"
    ])
    def test_edge_cases(self, solution: Solution, nums: list[int], 
                        expected_k: int, expected_nums: list[int]):
        k = solution.removeDuplicates(nums)
        assert k == expected_k
        assert nums[:k] == expected_nums

class TestRemoveDuplicatesFromSortedArray_NagitiveCases:
    """Test for the nagitive cases"""

    @pytest.mark.parametrize("nums, expected_errType, expected_errMsg",[
        ([101,101,102], ValueError, "value exceed upper bound"),
        ([-101,-101,-102], ValueError, "value exceed lower bound"),
        ([0]*30001, ValueError, "length exceed upper bound"),
        ([2,2,1,3,0,0,5,4], ValueError, "not sorted"),
        ([0,1,2,"a","b",3], TypeError, "contains non-integer"),
        ([], TypeError, "empty"),
        (0, TypeError, "not a list"),
    ], ids = [
        "Value exceed upper bound", 
        "Value exceed lower bound",
        "nums length exceed uper bound",
        "nums is not a sorted list",
        "nums contains non-integer value",
        "nums in empty",
        "nums is not a list",
    ])
    def test_nagitive_cases(self, solution: Solution, nums: list[int], 
                            expected_errType, expected_errMsg: str):
        with pytest.raises(Exception) as excinfo:
            k = solution.removeDuplicates(nums)
        assert excinfo.type == expected_errType
        assert expected_errMsg in str(excinfo.value)

class TestRemoveDuplicatesFromSortedArray_OutputValidation:
    """Test for output validation"""

    def test_output_validation(self, solution: Solution):
        nums = [0,0,1,2,3,3,4,5,5]
        origin_length = len(nums)
        k = solution.removeDuplicates(nums)
        # Validate for k
        assert isinstance(k, int)
        assert k >= 1
        assert k <= origin_length
        # Validate for nums
        assert isinstance(nums, list)
        assert nums != []
        assert nums[:k] == sorted(nums[:k])
        assert len(nums[:k]) == len(set(nums[:k]))
