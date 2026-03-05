---
name: new-leetcode-problem
description: Create a new LeetCode problem folder by copying templates and initializing README.md. Trigger when the user wants to add a new LeetCode problem.
disable-model-invocation: true
argument-hint: difficulty slug id "title" "link"
---

Help the user create a new LeetCode problem folder.

## Steps

1. If `$ARGUMENTS` is not empty, parse them in order as `difficulty slug id title link`.
   If `$ARGUMENTS` is empty or incomplete, ask the user for each missing field:
   - **difficulty**: easy / medium / hard
   - **slug**: problem slug, e.g. `two_sum` (use underscores, not spaces)
   - **id**: LeetCode problem number, e.g. `1`
   - **title**: problem title, e.g. `Two Sum`
   - **link**: LeetCode problem URL

2. Confirm the details with the user before running:
   ```
   difficulty : {difficulty}
   slug       : {slug}
   id         : {id}
   title      : {title}
   link       : {link}
   ```

3. Run the following command from the workspace root (activate venv first):
   ```bash
   source venv/Scripts/activate && python scripts/new_problem.py \
     --difficulty {difficulty} \
     --slug {slug} \
     --id {id} \
     --title "{title}" \
     --link "{link}"
   ```

4. Create an empty `__init__.py` in the new problem folder.
   Also ensure `__init__.py` exists in every parent directory up to (and including) `src/`:
   - `src/__init__.py`
   - `src/leetcode/__init__.py`
   - `src/leetcode/{difficulty}/__init__.py`
   - `src/leetcode/{difficulty}/{folder}/__init__.py`

5. Show the created folder path.
   Suggest next steps: open `solution.py` to start writing the solution, then use `/accompany-testcases` when ready to write test cases.
