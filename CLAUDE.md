# SDET Workspace

Practice workspace for SDET skills including LeetCode problems and interview preparation.

## Language Preference

- Communicate in **Traditional Chinese (繁體中文)**

## Project Structure

```
src/
  leetcode/
    _templates/       # Templates for new problems (solution.py, test_solution.py, README.md)
    easy/             # Easy difficulty problems
    SubmitCode/       # VS Code LeetCode extension submissions
  interview/
    pytest_drills/    # pytest exercises (day01~day06)
    mini_projects/    # Mini project exercises
scripts/
  new_problem.py      # Script to create new LeetCode problem folders
skills/               # ChatGPT skills config (not used by Claude Code)
notes/                # Notes
```

## Creating New LeetCode Problems

Use `scripts/new_problem.py`:

```bash
python scripts/new_problem.py --difficulty easy --slug two_sum --id 1 --title "Two Sum" --link "https://leetcode.com/problems/two-sum/"
```

The script copies from `_templates/` and automatically renames the test file to `test_{slug}.py`.

## Testing Conventions

- Use **pytest**
- Test files must have **unique names**: `test_{slug}.py` (never use `test_solution.py` to avoid module conflicts)
- `pyproject.toml` is configured to exclude `_templates` from collection
- Run all tests from root: `python -m pytest src/ -v`

## Python Environment

- Virtual environment at `venv/`
- Activate: `source venv/Scripts/activate` (bash) or `venv\Scripts\activate.bat` (cmd)

## Workflows

### Accompany Test Case Writing

Trigger phrases: "陪我寫測項", "陪我寫 testcases"

Steps:
1. Read the problem's `solution.py` and existing `test_*.py` to understand the CheckInput validation logic
2. Guide the user through four test categories:
   - Happy Path
   - Edge Cases
   - Negative Test (corresponding to CheckInput raise conditions)
   - Output Validation (verify return value type and content)
3. After the user finishes describing all test cases, draw a mermaid flowchart LR diagram and update the README.md Test Plan section

Mermaid format reference: `src/leetcode/easy/0026_remove_duplicates_from_sorted_array/README.md`
