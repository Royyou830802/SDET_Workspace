---
name: leetcode-problem-creator
description: Create a new LeetCode problem folder from workspace templates by running scripts/new_problem.py. Use when the user asks to add a LeetCode problem (e.g., "Add a LeetCode problem" or "Create a new leetcode"), set up a new problem folder, or copy LeetCode templates.
---

# LeetCode Problem Creator

## Overview

Create a new LeetCode problem folder using the workspace script `scripts/new_problem.py` and the templates in `src/leetcode/_templates`.

## Workflow

1. Collect required inputs:
   - `difficulty` (easy | medium | hard)
   - `slug` (e.g., `two_sum`)
2. Collect optional inputs:
   - `id` (numeric or string, used as prefix)
   - `title` (for README)
   - `link` (for README)
3. If any required input is missing, ask the user for it before running the script.
4. Run the script from the repo root with the Python launcher:

```bash
py scripts/new_problem.py --difficulty <easy|medium|hard> --slug <slug> [--id <id>] [--title "<title>"] [--link "<url>"]
```

5. Report the created folder path to the user.

## Examples

- User: "Add a LeetCode problem"
  - Ask for `difficulty` and `slug`.

- User: "Create a new leetcode: two sum (easy), id 1"
  - Run:

```bash
py scripts/new_problem.py --difficulty easy --slug two_sum --id 1
```
