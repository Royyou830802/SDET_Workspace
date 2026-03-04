import pytest
from solution import Solution

@pytest.fixture(scope = 'module')
def solution():
    return Solution()

class TestClimbingStairs_HappyPath():

    @pytest.mark.parametrize("input_n, expected_output",
    [
        (2, 2),
        (3, 3),
        (10, 89),
        (37, 39088169),
    ],
    ids = [
        "Example from the LeetCode case 1: input n = 2 -> output = 2.",
        "Example from the LeetCode case 2: input n = 3 -> output = 3.",
        "Test for medium number n: input n = 10 -> output = 89.",
        "Test for large number n: input n = 37 -> output = 39088169.",
    ])

    def test_happy_path(self, solution: Solution, input_n: int, expected_output: int):
        output = solution.climbStairs(input_n)
        assert output == expected_output
    
class TestClimbingStairs_EdgeCase():
    
    @pytest.mark.parametrize("input_n, expected_output",
    [
        (1, 1),
        (45, 1836311903),
    ],
    ids = [
        "Test for the smallest edge: input n = 1 -> expected output = 1.",
        "Test for the largest edge: input n = 45 -> expected output = 1836311903.",
    ])

    def test_edge_case(self, solution: Solution, input_n: int, expected_output: int):
        output = solution.climbStairs(input_n)
        assert output == expected_output

class TestClimbingStairs_NegitiveCase():

    @pytest.mark.parametrize("input_n, expected_ErrorType, expected_ErrorMsg",
    [
        (50, ValueError, "value is larger than 45"),
        (-10, ValueError, "value is smaller than 1"),
        ('10', TypeError, "not a integer"),
        (0, ValueError, "value is smaller than 1"),
        (None, TypeError, "not a integer"),
        (3.5, TypeError, "not a integer"),
    ],
    ids = [
        "Test for input n is larger than upper bound 45.",
        "Test for input n is smaller than lower bound 1.",
        "Test for input n is not an integer.",
        "Test for input n is equal = 0.",
        "Test for input n is a None.",
        "Test for input n is a float.",
    ])

    def test_negitive_case(self, solution: Solution, input_n: int, expected_ErrorType, expected_ErrorMsg: str):
        with pytest.raises(Exception) as exacinfo:
            solution.climbStairs(input_n)
        assert exacinfo.type == expected_ErrorType
        assert expected_ErrorMsg in str(exacinfo.value)

class TestClimbingStairs_OutputValidation():

    @pytest.mark.parametrize("validate_func, fail_reason",
    [
        (lambda out: isinstance(out, int), "Output is not a integer."),
        (lambda out: out > 0, "Output should not be smaller than 0."),
        (lambda out: out < 1836311904, "Output should not be larger than 1836311904."),
        (lambda out: out == 8, "Output is not correct."),
    ],
    ids = [
        "Validate whether the output is an integer.",
        "Validate the output is larger than 0.",
        "Validate the output is smaller than 1836311904.",
        "Validate the output is correct.",
    ])

    def test_output_validation(self, solution: Solution, validate_func, fail_reason: str):
        output = solution.climbStairs(5)
        assert validate_func(output), f"Failed: {fail_reason}"