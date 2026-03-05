# 70. Climbing Stairs

## Problem Description

You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?

**Constraints:**
- `1 <= n <= 45`

**Examples:**

```
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
  1. 1 step + 1 step
  2. 2 steps

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
  1. 1 step + 1 step + 1 step
  2. 1 step + 2 steps
  3. 2 steps + 1 step
```

## Approach

### Method: Dynamic Programming (Space-Optimized)

**Key idea:** This is essentially a Fibonacci sequence. To reach step n, you can only come from step n-1 or n-2, so `f(n) = f(n-1) + f(n-2)`. Use two variables to track previous states for O(1) space.

## Algorithm Flowchart

```mermaid
graph TD
    Start([Start: n]) --> Check{n <= 2?}
    Check -->|Yes| Return1[Return n]
    Check -->|No| Init[Initialize: prev2=1, prev1=2]
    Init --> Loop[Loop: i = 3 to n]
    Loop --> Calc[Calculate: current = prev1 + prev2]
    Calc --> Update[Update: prev2=prev1, prev1=current]
    Update --> Continue{i < n?}
    Continue -->|Yes| Loop
    Continue -->|No| Return2[Return prev1]
    Return1 --> End([End])
    Return2 --> End
```

## Step-by-Step Walkthrough

### DP 5-Step Framework

1. **State Definition**: `dp[i]` = number of ways to reach step i
2. **Recurrence Relation**: `dp[i] = dp[i-1] + dp[i-2]`
3. **Base Cases**: `dp[1] = 1`, `dp[2] = 2`
4. **Computation Order**: Bottom-up from 1 to n
5. **Final Answer**: `dp[n]`

### Example (n=5)

| Step i | Ways | Calculation |
|--------|------|-------------|
| 1 | 1 | base case |
| 2 | 2 | base case |
| 3 | 3 | 2 + 1 |
| 4 | 5 | 3 + 2 |
| 5 | 8 | 5 + 3 |

### Space Optimization

**Initial idea**: Sliding window with `pop(0)`
- Space: O(1) ✅ but Time: O(n²) ❌ (`pop(0)` is O(n))

**Final solution**: Two variables
- Space: O(1) ✅ and Time: O(n) ✅

## Implementation

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        prev2, prev1 = 1, 2
        for i in range(3, n + 1):
            prev2, prev1 = prev1, prev1 + prev2
        
        return prev1
```

## Complexity Analysis

| | Complexity | Explanation |
|-|------------|-------------|
| **Time** | O(n) | Loop runs n-2 times with O(1) operations |
| **Space** | O(1) | Only two variables used |

## Notes

### Key Insights
- Pattern recognition: This is Fibonacci sequence
- Space optimization: Only need last 2 states, not entire array
- Avoid `list.pop(0)` - it's O(n). Use variables or `deque` instead

## Test Plan

```mermaid
flowchart LR
    ROOT((climbStairs)) --> HP[Happy Path]
    ROOT --> EC[Edge Cases]
    ROOT --> NT[Negative Test]
    ROOT --> OV[Output Validation]

    HP --> HP1["n=2, expected=2"]
    HP --> HP2["n=3, expected=3"]
    HP --> HP3["n=10, expected=89"]
    HP --> HP4["n=37, expected=39088169"]

    HP1 --> HP1A[Example 1]
    HP2 --> HP2A[Example 2]
    HP3 --> HP3A[Medium number]
    HP4 --> HP4A[Large number]

    EC --> EC1["n=1, expected=1"]
    EC --> EC2["n=45, expected=1836311903"]

    EC1 --> EC1A[Minimum boundary]
    EC2 --> EC2A[Maximum boundary]

    NT --> NT1["n=50, ValueError"]
    NT --> NT2["n=-10, ValueError"]
    NT --> NT3["n='10', TypeError"]
    NT --> NT4["n=0, ValueError"]
    NT --> NT5["n=None, TypeError"]
    NT --> NT6["n=3.5, TypeError"]

    NT1 --> NT1A[Exceeds max]
    NT2 --> NT2A[Below min]
    NT3 --> NT3A[String input]
    NT4 --> NT4A[Just outside min boundary]
    NT5 --> NT5A[Null value]
    NT6 --> NT6A[Float input]

    OV --> OV0["Test input: n=5"]
    OV0 --> OV1[Type is int]
    OV0 --> OV2[Value > 0]
    OV0 --> OV3[Value < 1836311904]
    OV0 --> OV4[Value == 8]

    OV1 --> OV1A[Verify return type]
    OV2 --> OV2A[Verify positive result]
    OV3 --> OV3A[Verify within max range]
    OV4 --> OV4A[Verify correct calculation]
```

## Related Problems

- [746. Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/) — Same structure with cost weights
- [509. Fibonacci Number](https://leetcode.com/problems/fibonacci-number/) — Similar recurrence relation
- [198. House Robber](https://leetcode.com/problems/house-robber/) — Similar DP pattern

---

**Difficulty:** Easy
**Tags:** Math, Dynamic Programming, Memoization
