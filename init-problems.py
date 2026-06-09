#!/usr/bin/env python3
"""Initialize blank CSES solution files from cses.fi/problemset/."""

from __future__ import annotations

import argparse
import re
import sys
import urllib.request
from pathlib import Path

CSES_URL = "https://cses.fi/problemset/"
FILENAME_FMT = "{id}. {name}.py"


def fetch_sections(html: str) -> list[tuple[str, list[tuple[str, str]]]]:
    parts = re.split(r"<h2>", html)
    sections: list[tuple[str, list[tuple[str, str]]]] = []

    for part in parts[1:]:
        match = re.match(r"([^<]+)</h2>", part)
        if not match:
            continue

        name = match.group(1).strip()
        if name == "General":
            continue

        chunk = part.split("</ul>")[0] if "</ul>" in part else part
        tasks = re.findall(r'href="/problemset/task/(\d+)">([^<]+)</a>', chunk)
        sections.append((name, tasks))

    return sections


def problem_path(root: Path, section: str, task_id: str, task_name: str) -> Path:
    filename = FILENAME_FMT.format(id=task_id, name=task_name)
    return root / section / filename


def existing_ids(section_dir: Path) -> set[str]:
    ids: set[str] = set()
    if not section_dir.is_dir():
        return ids
    for path in section_dir.glob("*.py"):
        match = re.match(r"^(\d+)", path.name)
        if match:
            ids.add(match.group(1))
    return ids


def init_problems(root: Path, dry_run: bool = False) -> tuple[int, int, int]:
    with urllib.request.urlopen(CSES_URL, timeout=30) as response:
        html = response.read().decode()

    sections = fetch_sections(html)
    created = 0
    skipped = 0
    total = 0

    for section, tasks in sections:
        section_dir = root / section
        if not dry_run:
            section_dir.mkdir(parents=True, exist_ok=True)

        present = existing_ids(section_dir)

        for task_id, task_name in tasks:
            total += 1
            path = problem_path(root, section, task_id, task_name)

            if task_id in present or path.exists():
                skipped += 1
                continue

            if dry_run:
                print(f"Would create: {path.relative_to(root)}")
            else:
                path.write_text(f"# {task_id}. {task_name}\n")
                print(f"Created: {path.relative_to(root)}")

            present.add(task_id)
            created += 1

    return created, skipped, total


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "-n",
        "--dry-run",
        action="store_true",
        help="Show files that would be created without creating them",
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parent,
        help="Repository root (default: script directory)",
    )
    args = parser.parse_args()

    created, skipped, total = init_problems(args.root, dry_run=args.dry_run)
    action = "Would create" if args.dry_run else "Created"
    print(f"\n{action}: {created}, skipped (already exist): {skipped}, total: {total}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
