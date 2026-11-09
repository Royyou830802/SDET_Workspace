class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if type(s) != str:
            raise TypeError("Input is not a string.")
        elif len(s) == 0 or len(s) > 50000:
            raise ValueError("The lenth of input string is out of the range.")
        elif len(s) == 1: return 1
        
        left_ptr = 0
        max_length = 0
        str_length = len(s)
        for right_ptr in range(1, str_length):
            if s[right_ptr] in s[left_ptr:right_ptr]:
                left_ptr = right_ptr
            max_length = max(max_length, right_ptr - left_ptr + 1)
        return max_length