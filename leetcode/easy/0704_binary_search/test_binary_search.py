import pytest
from .solution import Solution


@pytest.fixture(scope='module')
def solution():
    return Solution()

@pytest.mark.parametrize(
    "inputList, target, expectResult",[
        ([-1,0,3,5,9,12], 9, 4),
        ([-1,0,3,9,12,15,18], 9, 3),
        ([-1,9,12,15,18], 9, 1),
    ], ids = [
        "Target at right",
        "Target at middle",
        "Target at left"
    ]
)                    
def test_binarysearch_happypath(solution, inputList, target, expectResult):
    result = solution.search(inputList, target)
    assert result == expectResult

list_10000 = list(range(1, 10001))
@pytest.mark.parametrize(
    "inputList, target, expectResult",[
        ([-1,0,3,5,9,12], 12, 5),
        ([-1,0,3,5,9,12], -1, 0),
        ([-1,0,3,5,9,12,10**4-1, 10**4], 9999, 6),
        (list_10000, 9999, 9998),
        ([-30], -30, 0),
        ([1], 10, -1)
    ], ids = [
        "Target at right edge",
        "Target is negative and at left edge",
        "Target is 9999",
        "Input list has 10000 items",
        "Only 1 item in list",
        "Target not in list"
    ]
)                 
def test_binarysearch_edgecase(solution, inputList, target, expectResult):
    result = solution.search(inputList, target)
    assert result == expectResult

list_10001 = list(range(10001))
@pytest.mark.parametrize(
    "inputList, target, ErrorType, ErrorMsg", [
        ([], 1, ValueError, "list is empty"),
        ([0]*10, 0, ValueError, "list is not unique"),
        (list_10001, 0, ValueError, "list length is larger than 10000"),
        ([10001], 10001, ValueError, "number in list is larger than 10^4"),
        ([0,1], 10001, ValueError, "target is larger than 10^4"),
        ([-10001], -10001, ValueError, "number in list is smaller than -10^4"),
        ([0,1], -10001, ValueError, "target is smaller than -10^4"),
        ([1.5], 1, TypeError, "list element is not integer"),
        ([1], 1.5, TypeError, "target is not integer"),
        ("abc", "a", TypeError, "input is not list"),
        ([0], "a", TypeError, "target is not integer")
    ]
)
def test_binarysearch_negative(solution, inputList, target, ErrorType, ErrorMsg):
    with pytest.raises(Exception) as exacInfo:
        solution.search(inputList, target)
    assert exacInfo.type == ErrorType
    assert str(exacInfo.value) == ErrorMsg