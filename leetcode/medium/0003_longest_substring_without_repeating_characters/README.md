# 3. Longest Substring Without Repeating Characters

## Problem Description

Given a string `s`, find the length of the **longest substring** without duplicate characters.

A **substring** is a contiguous non-empty sequence of characters within a string.

**Constraints:**
- `0 <= s.length <= 5 * 10⁴`
- `s` consists of English letters, digits, symbols and spaces

**Examples:**

```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

**Function Signature:**

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
```

## Hints

<details>
<summary>Hint 1</summary>

Checking every substring is O(n²) or worse. Can you keep a "window" of characters that has no duplicates?
</details>

<details>
<summary>Hint 2</summary>

Use two pointers `left` and `right`. Expand `right` one step at a time. When the new character is already in the window, how should `left` move?
</details>

<details>
<summary>Hint 3</summary>

A set tells you *whether* a character is in the window. A dict storing each character's last index tells you *where* — which lets `left` jump directly.
</details>

## Approach

_TODO_

## Complexity Analysis

_TODO_

## Test Plan

_TODO (use `/accompany-testcases`)_

## Related Problems

- [159. Longest Substring with At Most Two Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/)
- [340. Longest Substring with At Most K Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/)
- [424. Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)

---

**Difficulty:** Medium
**Tags:** Hash Table, String, Sliding Window
**LeetCode:** https://leetcode.com/problems/longest-substring-without-repeating-characters/
