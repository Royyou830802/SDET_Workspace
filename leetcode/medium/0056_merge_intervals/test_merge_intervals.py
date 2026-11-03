import pytest
from .solution import Solution


@pytest.fixture(scope='module')
def solution():
    return Solution()


@pytest.mark.skip("TODO: add tests")
def test_example(solution):
    pass
