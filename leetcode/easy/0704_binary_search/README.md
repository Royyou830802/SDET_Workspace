# 704. Binary Search

## Problem Description

Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return `-1`.

You must write an algorithm with `O(log n)` runtime complexity.

**Constraints:**
- `1 <= nums.length <= 10⁴`
- `-10⁴ < nums[i], target < 10⁴`
- All the integers in `nums` are **unique**
- `nums` is sorted in ascending order

**Examples:**

```
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
```

**Function Signature:**

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
```

## Hints

<details>
<summary>Hint 1</summary>

Compare `target` with the middle element. Which half can you throw away?
</details>

<details>
<summary>Hint 2</summary>

Decide on one invariant and stick with it: is your range `[left, right]` (closed) or `[left, right)` (half-open)? This determines whether the loop is `while left <= right` or `while left < right`.
</details>

<details>
<summary>Hint 3</summary>

Test your loop on arrays of length 1 and 2, and on targets smaller than the first / larger than the last element — that's where off-by-one bugs hide.
</details>

## Approach

_TODO_

## Complexity Analysis

_TODO_

## Test Plan

_TODO (use `/accompany-testcases`)_

## SDET Talking Point

The same idea powers `git bisect`: given a known-good commit and a known-bad commit, binary search the history to find the commit that introduced a regression in `O(log n)` builds/tests.

## Related Problems

- [35. Search Insert Position](https://leetcode.com/problems/search-insert-position/)
- [278. First Bad Version](https://leetcode.com/problems/first-bad-version/) — the `git bisect` problem
- [34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

---

**Difficulty:** Easy
**Tags:** Array, Binary Search
**LeetCode:** https://leetcode.com/problems/binary-search/
