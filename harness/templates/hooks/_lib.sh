# Locate _guard and REFUSE if it is not usable.
#
# A hook only runs where core.hooksPath points at this directory, so the harness
# is configured here and a missing or non-executable _guard is a defect, not
# permission. Exiting 0 would make the guard's absence indistinguishable from its
# consent — the same fail-open that was just closed inside _guard itself.
#
# The non-executable case is the one that actually happens: where core.fileMode
# is false, `chmod +x` succeeds on disk while git stores 100644, so the hooks
# arrive inert in every fresh clone and after every `git reset --hard`.
harness_guard() {
    G="$(git rev-parse --path-format=absolute --git-common-dir)/../.harness/hooks/_guard"
    if [ ! -e "$G" ]; then
        echo "harness-guard: _guard is missing at $G — refusing." >&2
        echo "  This repository is configured to use the harness, so its absence" >&2
        echo "  is a defect rather than permission. Restore it, or unset core.hooksPath." >&2
        return 1
    fi
    if [ ! -x "$G" ]; then
        echo "harness-guard: _guard is not executable — refusing." >&2
        echo "  git records the mode from its index, not from disk. Run:" >&2
        echo "    git update-index --chmod=+x .harness/hooks/*" >&2
        echo "  and commit, or every fresh clone ships an inert guard." >&2
        return 1
    fi
    printf '%s' "$G"
}
