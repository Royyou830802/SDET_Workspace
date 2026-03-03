#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
from collections import Counter

class Solution:
    def CheckInput(self, s: str, t: str):
        ## Check the input
        # Check the length of input s / t, should <= 50000 and > 1
        if len(s) > 5 * 10**4 or len(t) > 5 * 10**4:
            raise ValueError("The length of input exceed upper bound 50000")
        elif len(s) < 1 or len(t) < 1:
            raise ValueError("The length of input exceed lower bound 1")
        
        # Check all the characters in the s / t is lower
        if s.isupper() or t.isupper():
            raise TypeError("The input consist of uppercase English letters.")
        
    def isAnagram(self, s: str, t: str) -> bool:
        self.CheckInput(s, t)
        Cnt_s = Counter(s)
        Cnt_t = Counter(t)
        if Cnt_s == Cnt_t:
            return True
        else:
            return False
        
# @lc code=end

