---
name: accompany-testcases
description: Guide the user through writing LeetCode test cases across four categories — Happy Path, Edge Cases, Negative Test, Output Validation — then generate a mermaid diagram and update README.md. Trigger when the user says "陪我寫測項" or "陪我寫 testcases".
argument-hint: problem-folder-path
---

Guide the user through writing test cases for a LeetCode problem. Communicate in Traditional Chinese (繁體中文).

## Steps

### 1. Identify the problem folder

- If `$ARGUMENTS` is not empty, use that as the problem folder path.
- If empty, ask the user to provide the path (e.g. `src/leetcode/easy/0001_two_sum`).

### 2. Read existing files

Read the following files to understand the problem logic and current test structure:
- `{problem-folder}/solution.py` — understand the `CheckInput` validation rules and raise conditions
- `{problem-folder}/test_*.py` — understand existing test style and coverage

### 3. Guide through four test categories

Walk through each category one at a time:
- Explain the purpose of the category
- Ask the user to describe the scenarios they want to test
- Wait for confirmation before moving to the next category

**Category order:**

1. **Happy Path** — valid inputs that should execute successfully
2. **Edge Cases** — boundary values and extreme scenarios (e.g. max/min values, length of 1)
3. **Negative Test** — invalid inputs corresponding to each `CheckInput` raise condition, expected to raise exceptions
4. **Output Validation** — verify the return value's type and content are correct

### 4. Generate mermaid diagram and update README.md

After the user confirms all test cases:

1. Build a mermaid `flowchart LR` diagram covering all four categories. Follow this format:

```
flowchart LR
    ROOT(({function_name})) --> HP[Happy Path]
    ROOT --> EC[Edge Cases]
    ROOT --> NT[Negative Test]
    ROOT --> OV[Output Validation]

    HP --> HP1[scenario name]
    HP1 --> HP1A["specific input and expected output"]
    ...

    NT --> NT1[violated validation rule]
    NT1 --> NT1A["input raise error"]
    ...

    OV --> OV0["Test input: ..."]
    OV --> OVK[Validate return value]
    OVK --> OVK1[sub-item]
    ...
```

2. Replace the content of the `# Test Plan` section in `{problem-folder}/README.md` with the generated mermaid diagram.
