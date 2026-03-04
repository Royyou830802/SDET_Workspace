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

class TestValidAnagram_EdgeCase():
    
    @pytest.mark.parametrize("input_s, input_t, expected_output",[
        ('aaaaa'*5000 + 'bbbbb'*5000, 'a'*25000 + 'b'*25000, True),
        ('aaaaabbbbb'*5000, 'cccccddddd'*5000, False),
        ('s', 's', True),
        ('s', 't', False),
        ('s'*50000, 's', False),
        ('s', 't'*50000, False)
    ], ids = [
        "Both the length of s and t are 50000, and is anagram.",
        "Both the length of s and t are 50000, and is not anagram.",
        "Both the length of s and t are 1, and s == t.",
        "Both the length of s and t are 1, and s != t.",
        "The length of s is 50000, and the length of r is 1.",
        "The length of s is 1, and the length of r is 50000.",
    ])

    def test_edge_cases(self, solution: Solution, input_s: str, input_t: str, expected_output: bool):
        output = solution.isAnagram(input_s, input_t)
        assert output == expected_output

class TestValidAnagram_NegitiveCase():

    @pytest.mark.parametrize("input_s, input_t, expected_ErrorType, expected_ErrorMsg",
    [
        ('s'*50001, 't', ValueError, 'exceed upper bound'),
        ('s', 't'*50001, ValueError, 'exceed upper bound'),
        ('s'*50001, 't'*50001, ValueError, 'exceed upper bound'),
        ('', 't', ValueError, 'exceed lower bound'),
        ('s', '', ValueError, 'exceed lower bound'),
        ('', '', ValueError, 'exceed lower bound'),
        ('s'*50001, '', ValueError, 'exceed upper bound'),
        ('s', 't'*50001, ValueError, 'exceed upper bound'),
        ('Sss', 'Ttt', TypeError, 'uppercase'),
        ('abcd1234', '4321dcba', TypeError, 'non-alpha'),
        ('aa!@#', '!@#aa', TypeError, 'non-alpha'),
    ],
    ids = [
        "Length of input s or t larger upper bound 50000 case 1.",
        "Length of input s or t larger upper bound 50000 case 2.",
        "Length of input s or t larger upper bound 50000 case 2.",
        "Length of input s or t smaller lower bound 1 case 1.",
        "Length of input s or t smaller lower bound 1 case 2.",
        "Length of input s or t smaller lower bound 1 case 2.",
        "Length of input s > 50000, t < 1",
        "Length of input s < 1, t > 50000",
        "Uppercase character in input s or t",
        "Non-alphabet word in input s or t case 1",
        "Non-alphabet word in input s or t case 2",
    ])

    def test_negitive_cases(self, solution: Solution, input_s: str, input_t: str, expected_ErrorType, expected_ErrorMsg: str):
        with pytest.raises(Exception) as exacInfo:
            solution.isAnagram(input_s, input_t)
        assert exacInfo.type == expected_ErrorType
        assert expected_ErrorMsg in str(exacInfo.value) 

class TestValidAnagram_OutputValidation():

    @pytest.mark.parametrize("input_s, input_t, expected_output_type, expected_output",
    [
        ('sss', 'sss', bool, True),
        ('sss', 'ttt', bool, False),
    ],
    ids = [
        "Output validation case 1: input s = 'sss', input t = 'sss' -> output should be a bool and True",
        "Output validation case 1: input s = 'sss', input t = 'ttt' -> output should be a bool and False",
    ])
    
    def test_output_validation(self, solution: Solution, input_s: str, input_t: str, expected_output_type, expected_output: bool):
        output = solution.isAnagram(input_s, input_t)
        assert isinstance(output, expected_output_type)
        assert output == expected_output