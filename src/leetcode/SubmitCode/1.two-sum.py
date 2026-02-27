#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 使用字典來存儲已經遍歷過的數字和它們的索引
        num_map = {}

        # 遍歷陣列
        for i, num in enumerate(nums):
            # 計算需要的配對數字
            complement = target - num

            # 如果配對數字已經在字典中，返回兩個索引
            if complement in num_map:
                return [num_map[complement], i]

            # 將當前數字和索引存入字典
            num_map[num] = i

        # 題目保證有解，所以不會執行到這裡
        return []
# @lc code=end

