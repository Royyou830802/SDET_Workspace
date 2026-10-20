# 20. Valid Parentheses

## Problem Description

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

**Constraints:**
- `1 <= s.length <= 10⁴`
- `s` consists of parentheses only `'()[]{}'`

**Examples:**

```
Input: s = "()"
Output: true

Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false

Input: s = "([])"
Output: true

Input: s = "([)]"
Output: false
```

**Function Signature:**

```python
class Solution:
    def isValid(self, s: str) -> bool:
```

## Hints

<details>
<summary>Hint 1</summary>

The most recently opened bracket must be the first one to be closed. Which data structure follows "last in, first out"?
</details>

<details>
<summary>Hint 2</summary>

When you see a closing bracket, what should be on top of the stack? What if the stack is empty?
</details>

<details>
<summary>Hint 3</summary>

After scanning the whole string, what must be true about the stack for the string to be valid?
</details>

## Approach

_TODO_

## Complexity Analysis

_TODO_

## Test Plan

_TODO (use `/accompany-testcases`)_

## Related Problems

- [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)
- [32. Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/)
- [1249. Minimum Remove to Make Valid Parentheses](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/)

---

**Difficulty:** Easy
**Tags:** String, Stack
**LeetCode:** https://leetcode.com/problems/valid-parentheses/
