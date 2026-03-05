# SDET Workspace

Practice workspace for SDET skills including LeetCode problems and interview preparation.

## Project Structure

```
.claude/
  CLAUDE.md               # Claude Code project instructions
  skills/
    new-leetcode-problem/ # /new-leetcode-problem skill
    accompany-testcases/  # /accompany-testcases skill
src/
  leetcode/
    _templates/           # Templates for new problems
    easy/                 # Easy difficulty problems
    SubmitCode/           # VS Code LeetCode extension submissions
  interview/
    pytest_drills/        # pytest exercises (day01~day06)
    mini_projects/        # Mini project exercises
scripts/
  new_problem.py          # Script to create new LeetCode problem folders
skills/                   # ChatGPT skills config
notes/                    # Notes
```

## Setup

```bash
# Create and activate virtual environment
python -m venv venv
source venv/Scripts/activate  # bash
# venv\Scripts\activate.bat   # cmd
```

## Creating a New LeetCode Problem

```bash
python scripts/new_problem.py \
  --difficulty easy \
  --slug two_sum \
  --id 1 \
  --title "Two Sum" \
  --link "https://leetcode.com/problems/two-sum/"
```

## Running Tests

```bash
python -m pytest src/ -v
```

## Testing Conventions

- Test files must be named `test_{slug}.py` to avoid module conflicts
- `_templates/` is excluded from pytest collection
