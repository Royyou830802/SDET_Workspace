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
def test_example(solution, intervals, expected_result):
    assert solution.merge(intervals) == expected_result