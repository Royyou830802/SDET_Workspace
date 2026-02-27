# Problem

- Title: Remove Duplicates from Sorted Array
- Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
- Difficulty: easy

# Constraints

- `1 <= nums.length <= 3 * 10^4`
- `-100 <= nums[i] <= 100`
- `nums` is sorted in non-decreasing order

# Approach

- Key idea:
- Data structures:
- Edge cases:

# Complexity

- Time:
- Space:

# Test Plan

```mermaid
flowchart LR
    ROOT((removeDuplicates)) --> HP[Happy Path]
    ROOT --> EC[Edge Cases]
    ROOT --> NT[Negative Test]
    ROOT --> OV[Output Validation]

    HP --> HP1[With duplicates]
    HP --> HP2[No duplicates]
    HP --> HP3[All same]

    HP1 --> HP1A["nums=[1,1,2] k=2"]
    HP1 --> HP1B["nums=[0,0,1,1,1,2,2,3,3,4] k=5"]
    HP2 --> HP2A["nums=[3,4] k=2"]
    HP2 --> HP2B["nums=[3,4,5,6,7] k=5"]
    HP3 --> HP3A["nums=[1,1,1,1] k=1"]

    EC --> EC1[Large values]
    EC --> EC2[Negative values]
    EC --> EC3[Very long array]
    EC --> EC4[Single element]

    EC1 --> EC1A["nums=[11,11,95,95,98,99,99,100,100] k=5"]
    EC2 --> EC2A["nums=[-5,-5,-2,-2,-1,-1,0,1,1,2,5] k=7"]
    EC3 --> EC3A["nums=[0]*29999 k=1"]
    EC4 --> EC4A["nums=[57] k=1"]

    NT --> NT1[Value exceeds upper bound]
    NT --> NT2[Value below lower bound]
    NT --> NT3[Length exceeds upper bound]
    NT --> NT4[Not sorted]
    NT --> NT5[Contains non-integer]
    NT --> NT6[Empty array]

    NT1 --> NT1A["nums=[101,101,102] raise error"]
    NT2 --> NT2A["nums=[-101,-101,-102] raise error"]
    NT3 --> NT3A["nums=[0]*30001 raise error"]
    NT4 --> NT4A["nums=[2,2,1,3,0,0,5,4] raise error"]
    NT5 --> NT5A["nums=[0,1,2,a,b,3] raise error"]
    NT6 --> NT6A["nums=[] raise error"]

    OV --> OV0["Test input: nums=[0,0,1,2,3,3,4,5,5]"]
    OV --> OVK[Validate k]
    OV --> OVN[Validate nums]

    OVK --> OVK1[k is a single value]
    OVK --> OVK2[k type is int]
    OVK --> OVK3["k >= 1"]
    OVK --> OVK4["k <= original length of nums"]
    OVN --> OVN1[type is still list]
    OVN --> OVN2[not empty]
    OVN --> OVN3["nums[:k] is sorted in non-decreasing order"]
    OVN --> OVN4["nums[:k] contains no duplicates"]
```

# Notes

- Any pitfalls or alternative approaches.
- Negative Test cases assume input validation is not yet implemented in solution. Tests are expected to fail until validation is added.
