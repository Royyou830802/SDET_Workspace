# SDET Workspace

Practice workspace for SDET skills including LeetCode problems and interview preparation.

## Language Preference

- Communicate in **Traditional Chinese (繁體中文)**

## Project Structure

```
.claude/
  skills/
    new-leetcode-problem/   # /new-leetcode-problem skill
    accompany-testcases/    # /accompany-testcases skill
leetcode/
  _templates/               # Templates for new problems
  easy/                     # Easy difficulty problems
  SubmitCode/               # VS Code LeetCode extension submissions
  scripts/
    new_problem.py          # Script to create new LeetCode problem folders
interview/
  pytest_drills/            # pytest exercises (day01~day06)
  log_parser/               # Mini project: log parsing exercise
  sensor_cleaning/          # Mini project: sensor data cleaning exercise
automation/                 # SDET automation framework (WIP)
docs/                       # Notes and documentation
```

## Testing Conventions

- Use **pytest**
- Test files must have **unique names**: `test_{slug}.py` (never use `test_solution.py` to avoid module conflicts)
- `pyproject.toml` is configured to exclude `_templates` from collection
- Run all tests from root: `python -m pytest leetcode/ interview/ automation/ -v`

## Python Environment

- Virtual environment at `venv/`
- Activate: `source venv/Scripts/activate` (bash) or `venv\Scripts\activate.bat` (cmd)
