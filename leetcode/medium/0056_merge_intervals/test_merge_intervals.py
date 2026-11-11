import pytest
from .solution import Solution


@pytest.fixture(scope='module')
def solution():
    return Solution()


@pytest.mark.parametrize(
    ("intervals", "expected_result"), [
        ([[1,3],[2,6],[8,10],[15,18]], [[1,6],[8,10],[15,18]]),
        ([[1,4],[4,5]], [[1,5]]),
        ([[4,7],[1,4]], [[1,7]])
    ], ids=[
        "example1",
        "example2",
        "example3"
    ]
)
def test_listmerge_happypath(solution, intervals, expected_result):
    assert solution.merge(intervals) == expected_result

@pytest.mark.parametrize(
    ("intervals", "expected_result"), [
        ([[1, 5]], [[1, 5]]),
        ([[1, 5] for _ in range(10000)], [[1, 5]]),
        ([[0, 3], [2, 10], [10, 10000]], [[0, 10000]])
    ], ids=[
        "Single interval in intervals",
        "10000 interval in intervals",
        "Items range from 0 to 10000"
    ]
)
def test_listmerge_edgecases(solution, intervals, expected_result):
    assert solution.merge(intervals) == expected_result

@pytest.mark.parametrize(
    ("intervals", "ErrorType", "ErrorMessage"), [
        ("abc", TypeError, "Input intervals must be a list."),
        ([[1, 5], "abc", 123], TypeError, "All items in the input intervals must be a list."),
        ([["abc", 123]], TypeError, "All items in the interval must be a int."),
        ([[1, 5], [1, 2, 3]], ValueError, "There must be only 2 int in the interval."),
        ([[1, 5], [9999, 10001]], ValueError, "The interval [9999, 10001] is out of range."),
        ([[1, 5], [-5, 1]], ValueError, "The interval [-5, 1] is out of range."),
        ([[1, 5], [5, 1]], ValueError, "The interval [5, 1] is invalid."),
        ([[1, 5] for _ in range(10001)], ValueError, "The length of intervals is out of range."),
    ]
)
def test_listmerge_negitivecases(solution, intervals, ErrorType, ErrorMessage):
    with pytest.raises(Exception) as exacInfo:
        solution.merge(intervals)
    assert exacInfo.type == ErrorType
    assert str(exacInfo.value) == ErrorMessage
