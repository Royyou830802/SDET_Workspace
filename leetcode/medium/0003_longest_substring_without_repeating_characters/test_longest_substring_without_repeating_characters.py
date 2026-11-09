import pytest
from .solution import Solution


@pytest.fixture(scope='module')
def solution():
    return Solution()

@pytest.mark.parametrize(
    ('s', 'expected_length'), [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3)
    ], ids=[
        "example_1",
        "example_2", 
        "example_3"
    ])
def test_lengthOfLongestSubstring_HappyPath(solution, s, expected_length):
    assert solution.lengthOfLongestSubstring(s) == expected_length

@pytest.mark.parametrize(
    ('s', 'expected_length'),[
        ("a"*5*10**4, 1),
        ("a", 1)
    ], ids = [
        "The longest string",
        "The shortest string"
    ])
def test_lengthOfLongestSubstring_EdgeCase(solution, s, expected_length):
    assert solution.lengthOfLongestSubstring(s) == expected_length

@pytest.mark.parametrize(
    ('s', 'ErrorType', 'ErrorMessage'), [
        (123, TypeError, "Input is not a string."),
        ("a" * 50001, ValueError, "The lenth of input string is out of the range."),
        ("", ValueError, "The lenth of input string is out of the range."),
    ], ids = [
        "Input not string",
        "Input length > 50000",
        "Input is empty string",
    ])
def test_lengthOfLongestSubstring_NegitiveCase(solution, s, ErrorType, ErrorMessage):
    with pytest.raises(Exception) as excepInfo:
        solution.lengthOfLongestSubstring(s)
    assert excepInfo.type == ErrorType
    assert str(excepInfo.value) == ErrorMessage