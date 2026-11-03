# 56. Merge Intervals

## Problem Description

Given an array of `intervals` where `intervals[i] = [start_i, end_i]`, merge all overlapping intervals, and return *an array of the non-overlapping intervals that cover all the intervals in the input*.

**Constraints:**
- `1 <= intervals.length <= 10⁴`
- `intervals[i].length == 2`
- `0 <= start_i <= end_i <= 10⁴`

**Examples:**

```
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Input: intervals = [[4,7],[1,4]]
Output: [[1,7]]
Explanation: Intervals [1,4] and [4,7] are considered overlapping.
```

**Function Signature:**

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
```

## Hints

<details>
<summary>Hint 1</summary>

The input is not guaranteed to be sorted (see example 3). What happens if you sort by start time first?
</details>

<details>
<summary>Hint 2</summary>

After sorting, compare each interval with the **last** interval in your result. When do they overlap?
</details>

<details>
<summary>Hint 3</summary>

When merging, the new end is `max(last_end, current_end)` — not just `current_end`. Why? (Think of `[[1,10],[2,3]]`.)
</details>

## Approach

_TODO_

## Complexity Analysis

_TODO_

## Test Plan

_TODO (use `/accompany-testcases`)_

## Related Problems

- [57. Insert Interval](https://leetcode.com/problems/insert-interval/)
- [252. Meeting Rooms](https://leetcode.com/problems/meeting-rooms/)
- [435. Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)

---

**Difficulty:** Medium
**Tags:** Array, Sorting
**LeetCode:** https://leetcode.com/problems/merge-intervals/
