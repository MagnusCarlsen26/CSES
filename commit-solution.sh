#!/usr/bin/env bash
# Commit new CSES solution files following repo convention:
#   feat: <problem number>. <problem name>
# Stages the .py file and its matching .cph prob metadata.

set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"

DRY_RUN=false
FILES=()

usage() {
  cat <<'EOF'
Usage: commit-solution.sh [options] [file.py ...]

Commit untracked CSES solution files. Each file is committed separately with
message: feat: <basename without .py>

Options:
  -n, --dry-run   Show what would be committed without committing
  -h, --help      Show this help

With no file arguments, all untracked .py files in the repo are committed.
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    -n|--dry-run) DRY_RUN=true; shift ;;
    -h|--help) usage; exit 0 ;;
    -*) echo "Unknown option: $1" >&2; usage >&2; exit 1 ;;
    *) FILES+=("$1"); shift ;;
  esac
done

add_prob_files() {
  local py_file="$1"
  local dir base cph_dir prob

  dir="$(dirname "$py_file")"
  base="$(basename "$py_file")"
  cph_dir="$dir/.cph"

  [[ -d "$cph_dir" ]] || return 0

  shopt -s nullglob
  for prob in "$cph_dir/.$base"_*.prob; do
    if $DRY_RUN; then
      echo "  $prob"
    else
      git add "$prob"
    fi
  done
  shopt -u nullglob
}

commit_solution() {
  local py_file="$1"
  local name

  if [[ ! -f "$py_file" ]]; then
    echo "Error: file not found: $py_file" >&2
    return 1
  fi

  if [[ "$py_file" != *.py ]]; then
    echo "Error: not a Python file: $py_file" >&2
    return 1
  fi

  if git ls-files --error-unmatch "$py_file" &>/dev/null; then
    echo "Skipping already tracked file: $py_file"
    return 0
  fi

  name="$(basename "$py_file" .py)"

  if $DRY_RUN; then
    echo "Would commit: feat: $name"
    echo "  $py_file"
    add_prob_files "$py_file"
    return 0
  fi

  git add "$py_file"
  add_prob_files "$py_file"

  git commit -m "feat: $name"
  echo "Committed: feat: $name"
}

if [[ ${#FILES[@]} -eq 0 ]]; then
  while IFS= read -r -d '' py_file; do
    FILES+=("$py_file")
  done < <(git ls-files --others --exclude-standard -z -- '*.py')
fi

if [[ ${#FILES[@]} -eq 0 ]]; then
  echo "No untracked solution files to commit."
  exit 0
fi

for py_file in "${FILES[@]}"; do
  commit_solution "$py_file"
done
