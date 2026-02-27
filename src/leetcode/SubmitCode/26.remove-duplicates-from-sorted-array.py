#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for idx in range(1, len(nums)):
            if nums[k] != nums[idx]:
                k += 1
                nums[k] = nums[idx]
        k += 1
        return k
        
# @lc code=end

