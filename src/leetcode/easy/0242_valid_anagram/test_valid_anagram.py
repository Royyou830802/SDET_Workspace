import pytest
from solution import Solution

# Define the general usage conponents
@pytest.fixture(scope = 'module')
def solution():
    return Solution()

class TestValidAnagram_HappyPath():

    @pytest.mark.parametrize("input_s, input_t, expected_output",[
        ('anagram', 'nagaram', True),
        ('sssss', 'sssss', True),
        ('rat', 'car', False),
        ('sssss', 'ttttt', False),
        ('banana', 'nabnaananabbaa', False),
        ('sssss', 'ssssssssss', False),
    ], ids = [
        "Same length, and is anagram case 1: s = 'anagram', t = 'nagaram' -> expected output = True",
        "Same length, and is anagram case 2: s = 'sssss', t = 'sssss' -> expected output = True",
        "Same length, and is not anagram case 1.: s = 'rat', t = 'car' -> expected output = False",
        "Same length, and is not anagram case 2.: s = 'sssss', t = 'ttttt' -> expected output = False",
        "Differetn length case 1: s = 'banana', t = 'nabnaananabbaa' -> expected output = False",
        "Differetn length case 1: s = 'sssss', t = 'ssssssssss' -> expected output = False"
    ])

    def test_happy_path(self, solution: Solution, input_s: str, input_t: str, expected_output: bool):
        output = solution.isAnagram(input_s, input_t)
        assert output == expected_output