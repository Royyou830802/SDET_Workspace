"""Create a new LeetCode problem folder from templates.

Usage:
  python scripts/new_problem.py --difficulty easy --slug two_sum
  python scripts/new_problem.py --difficulty medium --slug "longest_substring" --id 3
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path


VALID_DIFFICULTIES = {"easy", "medium", "hard"}


def _sanitize_slug(raw: str) -> str:
    slug = raw.strip().lower()
    slug = slug.replace("-", "_")
    slug = re.sub(r"\s+", "_", slug)
    slug = re.sub(r"[^a-z0-9_]", "", slug)
    slug = re.sub(r"_+", "_", slug).strip("_")
    return slug


def _folder_name(slug: str, problem_id: str | None) -> str:
    if not problem_id:
        return slug
    if problem_id.isdigit():
        return f"{int(problem_id):04d}_{slug}"
    return f"{problem_id}_{slug}"


def _update_readme(readme_path: Path, title: str | None, link: str | None, difficulty: str) -> None:
    text = readme_path.read_text(encoding="utf-8")
    if title:
        text = re.sub(r"^- Title:.*$", f"- Title: {title}", text, flags=re.MULTILINE)
    if link:
        text = re.sub(r"^- Link:.*$", f"- Link: {link}", text, flags=re.MULTILINE)
    text = re.sub(r"^- Difficulty:.*$", f"- Difficulty: {difficulty}", text, flags=re.MULTILINE)
    readme_path.write_text(text, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a new LeetCode problem folder from templates.")
    parser.add_argument("--difficulty", required=True, help="easy | medium | hard")
    parser.add_argument("--slug", required=True, help="problem slug (e.g. two_sum)")
    parser.add_argument("--id", dest="problem_id", help="optional numeric id")
    parser.add_argument("--title", help="optional problem title for README")
    parser.add_argument("--link", help="optional problem link for README")
    parser.add_argument("--force", action="store_true", help="overwrite if folder exists")
    args = parser.parse_args()

    difficulty = args.difficulty.strip().lower()
    if difficulty not in VALID_DIFFICULTIES:
        print(f"Invalid difficulty: {args.difficulty}. Use easy, medium, or hard.", file=sys.stderr)
        return 2

    slug = _sanitize_slug(args.slug)
    if not slug:
        print("Slug is empty after sanitization.", file=sys.stderr)
        return 2

    repo_root = Path(__file__).resolve().parents[1]
    template_dir = repo_root / "src" / "leetcode" / "_templates"
    dest_dir = repo_root / "src" / "leetcode" / difficulty / _folder_name(slug, args.problem_id)

    if not template_dir.exists():
        print(f"Template directory not found: {template_dir}", file=sys.stderr)
        return 2

    if dest_dir.exists():
        if not args.force:
            print(f"Destination already exists: {dest_dir}", file=sys.stderr)
            return 2
        shutil.rmtree(dest_dir)

    dest_dir.mkdir(parents=True, exist_ok=True)

    for name in ("solution.py", "test_solution.py", "README.md"):
        shutil.copy2(template_dir / name, dest_dir / name)

    _update_readme(dest_dir / "README.md", args.title, args.link, difficulty)

    print(f"Created: {dest_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
