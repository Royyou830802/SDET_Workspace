from __future__ import annotations

from typing import Any


class Solution:
    
    def ExceptionCheck(self, nums):
        #Check whether nums is a list.
        if not isinstance(nums, list):
            raise TypeError("The nums is not a list.")
        #Check is nums is empty.
        if nums == []:
            raise TypeError("The nums is empty.")
        # Check whether the nums contains only int.
        if any(not isinstance(x, int) for x in nums):
            raise TypeError("The nums contains non-integer value.")
        # Check for x in nums should < 100 and > -100
        if any(x > 100 for x in nums):
            raise ValueError("The value exceed upper bound 100.")
        if any(x < -100 for x in nums):
            raise ValueError("The value exceed lower bound 100.")
        # Check the length for nums should <= 3*10^4
        if len(nums) > 30000:
            raise ValueError("The length exceed upper bound 30000.")
        # Check if the nums is sorted:
        if nums != sorted(nums):
            raise ValueError("The nums is not sorted.")
        
    def removeDuplicates(self, nums: List[int]) -> int:
        ## Exception Check for input nums
        self.ExceptionCheck(nums)

        ## Actually run the solution
        k = 0
        for idx in range(1, len(nums)):
            if nums[k] != nums[idx]:
                k += 1
                nums[k] = nums[idx]
        k += 1
        return k
