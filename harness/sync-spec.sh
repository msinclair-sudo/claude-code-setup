#!/usr/bin/env bash
# Keep the bundled spec in step with the authoring note — and keep it SINGULAR.
#
# There is exactly one copy of the spec in the skills tree:
#
#     skills/harness/ref/spec.md
#
# The role skills (-upward, -downward, -root) deliberately carry none. They are
# never installed without `harness` and cannot function without it — `whoami` is
# what names them — so a private copy bought no portability. It bought four files
# to keep in step, and a session loading two roles reading the same 30 KB twice
# without being able to tell it had.
#
#   sync-spec.sh --from PATH   refresh the canonical copy from the authoring note
#   sync-spec.sh --check       exit 1 if canonical drifted, or a role re-grew one
#   sync-spec.sh               same as --check
#
# Authoring note: "Agent Workstream Harness.md" in the Obsidian vault.

set -e
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CANON="$DIR/skills/harness/ref/spec.md"
ROLES=(harness-upward harness-downward harness-root)
FROM=""
MODE=check

while [[ $# -gt 0 ]]; do
    case "$1" in
        --check) MODE=check; shift ;;
        --from)  [[ -f "$2" ]] || { echo "ERROR: no such file: $2" >&2; exit 1; }
                 FROM="$2"; MODE=from; shift 2 ;;
        -h|--help) sed -n '2,20p' "$0"; exit 0 ;;
        *) echo "ERROR: unknown option: $1" >&2; exit 1 ;;
    esac
done

fail=0

if [[ "$MODE" == from ]]; then
    cp "$FROM" "$CANON"
    echo "canonical refreshed from $FROM"
fi

[[ -f "$CANON" ]] || { echo "ERROR: canonical spec missing: $CANON" >&2; exit 1; }

# The invariant this script now exists to protect: nobody re-duplicates it.
for r in "${ROLES[@]}"; do
    stray="$DIR/skills/$r/ref/spec.md"
    if [[ -e "$stray" ]]; then
        echo "  RE-DUPLICATED: skills/$r/ref/spec.md"
        echo "    The role skills must not carry a spec. Delete it and point the"
        echo "    SKILL.md at ~/.claude/skills/harness/ref/spec.md instead."
        fail=1
    fi
done

# Every role skill must actually point somewhere reachable.
for r in "${ROLES[@]}"; do
    f="$DIR/skills/$r/SKILL.md"
    [[ -f "$f" ]] || continue
    if ! grep -q 'skills/harness/ref/spec.md' "$f"; then
        echo "  NO POINTER: skills/$r/SKILL.md does not reference the shared spec"
        fail=1
    fi
    if grep -qE '^Spec: `ref/spec\.md`' "$f"; then
        echo "  STALE POINTER: skills/$r/SKILL.md still points at its own ref/"
        fail=1
    fi
done

if [[ -n "$FROM" ]] && ! cmp -s "$FROM" "$CANON"; then
    echo "  DRIFTED: canonical differs from $FROM"; fail=1
fi

if [[ $fail -eq 0 ]]; then
    echo "ok — one spec, $(wc -c < "$CANON") bytes, $(( $(grep -c '^#\{2,3\} ' "$CANON") )) headings; 3 role skills point at it"
else
    exit 1
fi
