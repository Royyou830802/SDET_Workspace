from typing import List
import math
from collections import Counter

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Some preventions
        length = len(nums)
        if type(nums) != list:
            raise TypeError("input is not list")
        elif any(type(x) != int for x in nums):
            raise TypeError("list element is not integer")
        elif type(target) != int:
            raise TypeError("target is not integer")
        elif nums == []:raise ValueError("list is empty")
        elif any([x for x in Counter(nums).values() if x > 1]):
            raise ValueError("list is not unique")
        elif length > 10000:
            raise ValueError("list length is larger than 10000")
        elif max(nums) > 10000:
            raise ValueError("number in list is larger than 10^4")
        elif target > 10000:
            raise ValueError("target is larger than 10^4")
        elif min(nums) < -10000:
            raise ValueError("number in list is smaller than -10^4")
        elif target < -10000:
            raise ValueError("target is smaller than -10^4")
        
        
        # # return -1 if target not in the given list
        # if target not in nums: return -1
        
        # n = length
        # # get the middle point of the list
        # idx = math.floor(n/2)
        # # if the middle point is great than target
        # if nums[idx] > target:
        #     # search the left side of the list
        #     return self.search(nums[:idx], target)
        # # otehrwide small than target
        # elif nums[idx] < target:
        #     # search the right side of the list, and plus the length of left side
        #     return idx + self.search(nums[idx:], target)
        # # Finally if the middle point == target
        # else:
        #     return idx

        left, right = 0, length - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1