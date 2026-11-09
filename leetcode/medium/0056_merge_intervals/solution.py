from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not isinstance(intervals, list):
            raise TypeError("Input intervals must be a list.")
        for interval in intervals:
            if not isinstance(interval, list):
                raise TypeError("All items in the input intervals must be a list.")
            if not all([isinstance(x, int) for x in interval]):
                raise TypeError("All items in the interval must be a int.")
            if len(interval) != 2:
                raise ValueError("There must be only 2 int in the interval.")
            if interval[0] < 0 or interval[1] > 10000:
                raise ValueError(f"The interval {interval} is out of range.")
            if interval[1] < interval[0]:
                raise ValueError(f"The interval {interval} is invalid.")
        Length = len(intervals)
        if Length > 10000 or Length < 1:
            raise ValueError("The length of intervals is out of range.")

        intervals.sort(key= lambda x: x[0])
        result = [intervals[0]]
        for interval in intervals[1:]:
            if interval[0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                result.append(interval)
        return result