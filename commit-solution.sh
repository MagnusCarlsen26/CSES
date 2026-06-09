#!/usr/bin/env bash
# Commit CSES solution files following repo convention:
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

Commit CSES solution files. Each file is committed separately with message:
feat: <basename without .py>

Options:
  -n, --dry-run   Show what would be committed without committing
  -h, --help      Show this help

With no file arguments, commits all new or modified solution .py files.
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

is_solution_file() {
  [[ "$1" == */*.py ]]
}

prob_files_for() {
  local py_file="$1"
  local dir base cph_dir

  dir="$(dirname "$py_file")"
  base="$(basename "$py_file")"
  cph_dir="$dir/.cph"

  [[ -d "$cph_dir" ]] || return 0

  shopt -s nullglob
  printf '%s\0' "$cph_dir/.$base"_*.prob
  shopt -u nullglob
}

file_has_changes() {
  local file="$1"

  if [[ ! -e "$file" ]]; then
    return 1
  fi

  if ! git ls-files --error-unmatch "$file" &>/dev/null; then
    return 0
  fi

  ! git diff --quiet -- "$file" || ! git diff --cached --quiet -- "$file"
}

solution_has_changes() {
  local py_file="$1"
  local prob

  file_has_changes "$py_file" && return 0

  while IFS= read -r -d '' prob; do
    file_has_changes "$prob" && return 0
  done < <(prob_files_for "$py_file")

  return 1
}

collect_changed_solutions() {
  local -n _out=$1
  local seen=$'\n'
  local file

  add_file() {
    local candidate="$1"
    is_solution_file "$candidate" || return 0
    solution_has_changes "$candidate" || return 0
    [[ "$seen" == *$'\n'"$candidate"$'\n'* ]] && return 0
    seen+="$candidate"$'\n'
    _out+=("$candidate")
  }

  while IFS= read -r -d '' file; do
    add_file "$file"
  done < <(git ls-files --others --exclude-standard -z -- '*.py')

  while IFS= read -r -d '' file; do
    add_file "$file"
  done < <(git diff --name-only -z -- '*.py')

  while IFS= read -r -d '' file; do
    add_file "$file"
  done < <(git diff --cached --name-only -z -- '*.py')
}

stage_prob_files() {
  local py_file="$1"
  local prob

  while IFS= read -r -d '' prob; do
    if $DRY_RUN; then
      echo "  $prob"
    elif file_has_changes "$prob"; then
      git add "$prob"
    fi
  done < <(prob_files_for "$py_file")
}

commit_solution() {
  local py_file="$1"
  local name

  if [[ ! -f "$py_file" ]]; then
    echo "Error: file not found: $py_file" >&2
    return 1
  fi

  if ! is_solution_file "$py_file"; then
    echo "Error: not a solution file: $py_file" >&2
    return 1
  fi

  if ! solution_has_changes "$py_file"; then
    echo "Skipping (no changes): $py_file"
    return 0
  fi

  name="$(basename "$py_file" .py)"

  if $DRY_RUN; then
    echo "Would commit: feat: $name"
    echo "  $py_file"
    stage_prob_files "$py_file"
    return 0
  fi

  git add "$py_file"
  stage_prob_files "$py_file"

  if git diff --cached --quiet; then
    echo "Skipping (nothing staged): $py_file"
    return 0
  fi

  git commit -m "feat: $name"
  echo "Committed: feat: $name"
}

if [[ ${#FILES[@]} -eq 0 ]]; then
  collect_changed_solutions FILES
fi

if [[ ${#FILES[@]} -eq 0 ]]; then
  echo "No changed solution files to commit."
  exit 0
fi

for py_file in "${FILES[@]}"; do
  commit_solution "$py_file"
done
