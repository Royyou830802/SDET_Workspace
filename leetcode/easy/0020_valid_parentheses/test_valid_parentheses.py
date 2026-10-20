import pytest
from .solution import Solution


@pytest.fixture(scope='module')
def solution():
    return Solution()


@pytest.mark.parametrize(
    "input_string, expect_output", [
        ("{[()]}", True),
        ("()[]{}", True),
        ("([)]", False),
        ("(((", False),
        ("]", False)
    ], ids = [
        "Valid parenthese 1",
        "Valid parenthese 2",
        "Invalid parentese 1",
        "Invalid parentese 2",
        "Invalid parentese 3",
    ])
def test_validate_parenthese_happypath(solution, input_string, expect_output):
    assert solution.isValid(input_string) == expect_output

@pytest.mark.parametrize(
    "input_str, expect_output",[
        ("(", False),
        ("()"*5000, True),
    ], ids = [
        "Minimum length of str",
        "Maximum length of str"
    ]
)
def test_validate_parenthese_edgecase(solution, input_str, expect_output):
    assert solution.isValid(input_str) == expect_output

@pytest.mark.parametrize(
    "input_str, ErrorType, ErrorMessage", [
        (123, TypeError, "Input should be a string."),
        ("abc", ValueError, "Input should only contain parentheses."),
        ("()"*5001, ValueError, "Input length should be no more than 10^4."),
        ("", ValueError, "Input length should be larger than 0.")
    ]
)
def test_validate_parenthese_negitive(solution, input_str, ErrorType, ErrorMessage):
    with pytest.raises(Exception) as exacInfo:
        solution.isValid(input_str)
    assert exacInfo.type == ErrorType
    assert str(exacInfo.value) == ErrorMessage

def test_validate_parenthese_outputcheck(solution):
    s = "{}"
    result = solution.isValid(s)
    assert type(result) == bool
