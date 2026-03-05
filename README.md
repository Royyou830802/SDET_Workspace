# SDET Workspace

Personal workspace for building and demonstrating SDET skills — automation framework, system testing, pytest patterns, and LeetCode algorithm practice.

## Structure

```
automation/                   # SDET automation framework
  framework/
    utils/                    # subprocess_helper — wraps subprocess.run()
    collectors/               # Log collectors (mock / SSH)
    parsers/                  # Log parsers (app log / dmesg)
    fixtures/                 # Sample log files for testing
  system_tests/
    test_smoke.py             # Smoke tests — verify local tool availability

interview/                    # pytest drills and mini projects
  pytest_drills/              # pytest exercises (day01~day06)
  log_parser/                 # Mini project: log parsing exercise
  sensor_cleaning/            # Mini project: sensor data cleaning exercise

leetcode/                     # LeetCode problem solutions
  easy/
  _templates/                 # Templates for new problems
  scripts/
    new_problem.py            # Script to create new problem folders

docs/                         # Notes and documentation
```

## Setup

```bash
python -m venv venv
source venv/Scripts/activate  # bash
# venv\Scripts\activate.bat   # cmd

pip install -r pip_requirement.txt
```

## Running Tests

```bash
python -m pytest leetcode/ interview/ automation/ -v
```

## Creating a New LeetCode Problem

```bash
python leetcode/scripts/new_problem.py \
  --difficulty easy \
  --slug two_sum \
  --id 1 \
  --title "Two Sum" \
  --link "https://leetcode.com/problems/two-sum/"
```

## Testing Conventions

- Test files must be named `test_{slug}.py` to avoid module conflicts
- `leetcode/_templates/` is excluded from pytest collection
