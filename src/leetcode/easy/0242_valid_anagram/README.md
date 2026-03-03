# 242. Valid Anagram

## Problem Description

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

An **anagram** is a word formed by rearranging the letters of another word, using all the original letters exactly once.

**Constraints:**
- `1 <= s.length, t.length <= 5 * 10⁴`
- `s` and `t` consist of lowercase English letters only

**Examples:**

```
Input: s = "anagram", t = "nagaram"
Output: true
Explanation: "nagaram" is a rearrangement of all letters in "anagram"

Input: s = "rat", t = "car"
Output: false
Explanation: "rat" and "car" have different letter compositions
```

## Approach

### Method: Character Frequency Comparison (Counter / Hash Map) ✅

**Key idea:** An anagram has the exact same character frequencies as the original string.

Count the frequency of each character in both strings. If the frequency distributions are identical, `t` is an anagram of `s`.

## Algorithm Flowchart

```mermaid
graph TD
    Start([Start]) --> CountS[Counter: count char frequencies in s]
    CountS --> CountT[Counter: count char frequencies in t]
    CountT --> Compare{Cnt_s == Cnt_t?}
    Compare -->|Yes| RetTrue[Return True]
    Compare -->|No| RetFalse[Return False]
    RetTrue --> End([End])
    RetFalse --> End
```

## Step-by-Step Walkthrough

Using `s = "anagram"`, `t = "nagaram"`:

| Step | Operation | Result |
|------|-----------|--------|
| 1 | `Counter("anagram")` | `{'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1}` |
| 2 | `Counter("nagaram")` | `{'n': 1, 'a': 3, 'g': 1, 'r': 1, 'm': 1}` |
| 3 | Compare both Counters | Contents are equal → `True` ✅ |

Using `s = "rat"`, `t = "car"` (counter-example):

| Step | Operation | Result |
|------|-----------|--------|
| 1 | `Counter("rat")` | `{'r': 1, 'a': 1, 't': 1}` |
| 2 | `Counter("car")` | `{'c': 1, 'a': 1, 'r': 1}` |
| 3 | Compare both Counters | `'t'` vs `'c'` differ → `False` ❌ |

## Implementation

```python
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Cnt_s = Counter(s)
        Cnt_t = Counter(t)
        if Cnt_s == Cnt_t:
            return True
        else:
            return False
```

## Complexity Analysis

| | Complexity | Explanation |
|-|------------|-------------|
| **Time** | O(n) | Iterate through both strings once to build Counters |
| **Space** | O(1) | Counter holds at most 26 lowercase letters — constant size |

**Approach Comparison:**

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Sort and compare | O(n log n) | O(n) | `sorted(s) == sorted(t)` |
| Counter comparison | O(n) | O(1) | This solution ✅ |
| Manual count array | O(n) | O(1) | Use a length-26 list to count |

## Notes

- **Why does Counter comparison work?**
  `Counter` is a subclass of `dict`. Comparing two Counters checks that every key-value pair is identical — any difference in character frequency returns `False`.

- **Common pitfall — `^` vs `**` in Python:**
  ```python
  5 * 10^4   # ❌ Bitwise XOR: 50 XOR 4 = 54
  5 * 10**4  # ✅ Exponentiation: 50000
  ```

- **`isupper()` behavior:**
  ```python
  "Hello".isupper()  # False — has lowercase letters
  "HELLO".isupper()  # True
  # For strict lowercase validation, prefer s.islower()
  ```

## Test Plan

```mermaid
flowchart LR
    ROOT((isAnagram)) --> HP[Happy Path]
    ROOT --> EC[Edge Cases]
    ROOT --> NT[Negative Test]
    ROOT --> OV[Output Validation]

    HP --> HP1[Same length, is anagram]
    HP --> HP2[Same length, not anagram]
    HP --> HP3[Different length]

    HP1 --> HP1A["s='anagram', t='nagaram' → True"]
    HP1 --> HP1B["s='sssss', t='sssss' → True"]
    HP2 --> HP2A["s='rat', t='car' → False"]
    HP2 --> HP2B["s='sssss', t='ttttt' → False"]
    HP3 --> HP3A["s='banana', t='nabnaananabbaa' → False"]
    HP3 --> HP3B["s='sssss', t='ssssssssss' → False"]

    EC --> EC1[Both len=50000]
    EC --> EC2[Both len=1]
    EC --> EC3[Asymmetric length]

    EC1 --> EC1A["s='aaaaa'*5000+'bbbbb'*5000, t='bbbbbaaaaa'*5000 → True"]
    EC1 --> EC1B["s='aaaaabbbbb'*5000, t='cccccddddd'*5000 → False"]
    EC2 --> EC2A["s='s', t='s' → True"]
    EC2 --> EC2B["s='s', t='t' → False"]
    EC3 --> EC3A["s='s'*50000, t='s' → False"]
    EC3 --> EC3B["s='s', t='s'*50000 → False"]

    NT --> NT1[Exceeds upper bound]
    NT --> NT2[Below lower bound]
    NT --> NT3[Mixed bounds]
    NT --> NT4[Contains uppercase]
    NT --> NT5[Contains non-alpha]

    NT1 --> NT1A["s='s'*50001, t='t' → ValueError upper bound"]
    NT1 --> NT1B["s='s', t='t'*50001 → ValueError upper bound"]
    NT1 --> NT1C["s='s'*50001, t='t'*50001 → ValueError upper bound"]
    NT2 --> NT2A["s='', t='t' → ValueError lower bound"]
    NT2 --> NT2B["s='s', t='' → ValueError lower bound"]
    NT2 --> NT2C["s='', t='' → ValueError lower bound"]
    NT3 --> NT3A["s='s'*50001, t='' → ValueError upper bound"]
    NT3 --> NT3B["s='', t='t'*50001 → ValueError upper bound"]
    NT4 --> NT4A["s='Sss', t='Ttt' → TypeError uppercase"]
    NT5 --> NT5A["s='abcd1234', t='4321dcba' → TypeError non-alpha"]
    NT5 --> NT5B["s='aa!@#', t='!@#aa' → TypeError non-alpha"]

    OV --> OVR[Return type is bool]
    OVR --> OVR1["s='sss', t='sss' → isinstance result bool True"]
    OVR --> OVR2["s='sss', t='ttt' → isinstance result bool True"]
```

## Related Problems

- [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/) — Group all anagram strings together
- [438. Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) — Find all anagram substrings
- [383. Ransom Note](https://leetcode.com/problems/ransom-note/) — Similar character frequency counting

---

**Difficulty:** Easy
**Tags:** Hash Table, String, Sorting
**Solution:** Counter Comparison (Hash Map)