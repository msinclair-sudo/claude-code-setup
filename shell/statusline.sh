#!/bin/bash
# Claude Code statusline
# Line 1: model | 🪪 session name (cyan, when known)  |  📁 project folder | 🌿 git branch (when in a repo)
# Line 2: 5h: N%  7d: N% (Pro/Max only, when present)
# Line 3: context bar 0-50% half — blue ▁ fill (used) / uncoloured ⣀ track (free)
# Line 4: context bar 51-100% half — red ▔ fill (used) / uncoloured ⠉ track (free)
# Each row is 50 chars wide (1% per char) so together they give 1%
# resolution across the full 0-100% range.
# Line 5: harness tree position (only in an enrolled repo; absent otherwise —
# see michaels_setup/harness/statusline-snippet.py, inlined here to avoid a
# runtime dependency on the harness CLI being installed).
input=$(cat)

_parsed=$(echo "$input" | python3 -c "
import json, sys, os, glob, re, subprocess
d = json.load(sys.stdin)
model = d.get('model', {}).get('display_name', '')
ws = d.get('workspace', {})
cdir = ws.get('project_dir') or ws.get('current_dir') or d.get('cwd', '')
pct = int(d.get('context_window', {}).get('used_percentage') or 0)
sid = d.get('session_id', '')

# Absent for non-Pro/Max plans and before the session's first API response.
rate_limits = d.get('rate_limits', {})
five_hour = rate_limits.get('five_hour', {}).get('used_percentage')
five_hour = '' if five_hour is None else str(int(five_hour))
seven_day = rate_limits.get('seven_day', {}).get('used_percentage')
seven_day = '' if seven_day is None else str(int(seven_day))

# Session name (as seen by other agents/sessions) lives in
# ~/.claude/sessions/<pid>.json, keyed by the harness process's PID, not by
# session_id. Try the fast path via \$CLAUDE_PID first, then fall back to
# scanning for a matching sessionId.
name = ''
sessions_dir = os.path.expanduser('~/.claude/sessions')
pid = os.environ.get('CLAUDE_PID', '')
if sid:
    candidate = os.path.join(sessions_dir, f'{pid}.json') if pid else ''
    try:
        if candidate and os.path.isfile(candidate):
            with open(candidate) as fh:
                s = json.load(fh)
            if s.get('sessionId') == sid:
                name = s.get('name', '')
        if not name:
            for f in glob.glob(os.path.join(sessions_dir, '*.json')):
                try:
                    with open(f) as fh:
                        s = json.load(fh)
                except Exception:
                    continue
                if s.get('sessionId') == sid:
                    name = s.get('name', '')
                    break
    except Exception:
        pass

# Things only the operator can clear, across EVERY enrolled project — not just
# this one, and not only inside a repository. A blocked lane that is only
# visible where it happened is one the operator finds hours later, so this reads
# the machine-wide derived file (needs.json, rebuilt by the harness whenever a
# block is raised, granted or resolved) rather than walking any project. Same
# contract as everything else here: '' for any reason at all, never raise.
def needs_badge():
    RED, RST = '\033[31m', '\033[0m'
    try:
        f = os.path.expanduser('~/.claude/harness/needs.json')
        if not os.path.isfile(f):
            return ''
        n = int(json.load(open(f)).get('count') or 0)
        if n < 1:
            return ''
        return RED + '\u26a0 ' + str(n) + ' need' + ('s' if n == 1 else '') + ' you' + RST
    except Exception:
        return ''


# Harness tree position — contract: return '' for ANY reason it can't produce
# a segment (not a repo, not enrolled, no index, branch not a node, malformed
# state). Never raise. '!N' (N sessions sharing one worktree) is coloured red.
# The needs badge is joined on here rather than printed as its own line so the
# shell side keeps parsing a fixed number of lines; it survives an empty
# position, which is the case that matters, since the operator is usually not
# standing in the repository that wants them.
def harness_segment(cdir):
    RED, RST = '\033[31m', '\033[0m'
    try:
        r = subprocess.run(
            ['git', '-C', cdir, 'rev-parse', '--path-format=absolute',
             '--git-common-dir', '--abbrev-ref', 'HEAD'],
            capture_output=True, text=True, timeout=2)
        if r.returncode:
            return ''
        common, branch = r.stdout.split('\n')[0].strip(), r.stdout.split('\n')[1].strip()
        repo = os.path.dirname(common.rstrip('/'))
        slug = re.sub(r'[^A-Za-z0-9]', '-', repo)
        idx_path = os.path.expanduser(f'~/.claude/harness/{slug}/index.json')
        if not os.path.isfile(idx_path):
            return ''
        idx = json.load(open(idx_path))
        node = idx.get('byBranch', {}).get(branch)
        if not node:
            return ''
        me = idx['nodes'][node]

        occ = {}
        by_wt = idx.get('byWorktree', {})
        for f in glob.glob(os.path.expanduser('~/.claude/sessions/*.json')):
            try:
                sd = json.load(open(f))
                os.kill(sd['pid'], 0)
            except Exception:
                continue
            # The daemon parks a warm spare process which also writes a session
            # file with cwd set to the repo. Counting it raised a false !2 on
            # main -- an I1 alarm with no violation behind it. A spare is
            # auto-named after its own jobId; harness sessions are named
            # project-node by spawn. NOTE: no backticks in this block; the
            # python is inside a double-quoted shell string and they would be
            # run as command substitution.
            if not sd.get('name') or sd.get('name') == sd.get('jobId'):
                continue
            n = by_wt.get(sd.get('cwd', ''))
            if n:
                occ.setdefault(n, []).append(sd)

        mark_glyph = {'busy': '•', 'idle': '◦'}
        # A node named in tree.json is a DECLARATION. A position exists only when
        # a live session stands in it and derives it from git (R1), so an
        # unoccupied node is not rendered at all. A lead with no children running
        # shows no children, which is the true statement. Use harness index to
        # see the declared tree.
        def mark(n):
            ss = occ.get(n, [])
            if not ss:
                return None
            if len(ss) > 1:
                return f'{n}{RED}!{len(ss)}{RST}'
            return n + mark_glyph.get(ss[0].get('status'), '?')

        def group(glyph, names):
            held = [m for m in (mark(n) for n in names) if m]
            return glyph + ' ' + ' '.join(held) if held else None

        bits = []
        up = mark(me['parent']) if me.get('parent') else None
        if up:
            bits.append('↑' + up)
        bits.append(f'[{node}]')
        for glyph, key in (('⇄', 'siblings'), ('↓', 'children')):
            g = group(glyph, me.get(key) or [])
            if g:
                bits.append(g)
        return '  '.join(bits)
    except Exception:
        return ''


def harness_line(cdir):
    parts = [x for x in (harness_segment(cdir), needs_badge()) if x]
    return '  '.join(parts)

print(model)
print(cdir)
print(pct)
print(name)
print(five_hour)
print(seven_day)
print(harness_line(cdir))
")

MODEL=$(echo "$_parsed"    | sed -n '1p')
DIR=$(echo "$_parsed"      | sed -n '2p')
PCT=$(echo "$_parsed"      | sed -n '3p')
SESSION_NAME=$(echo "$_parsed" | sed -n '4p')
FIVE_HOUR=$(echo "$_parsed" | sed -n '5p')
SEVEN_DAY=$(echo "$_parsed" | sed -n '6p')
HARNESS_LINE=$(echo "$_parsed" | sed -n '7p')

BRANCH=$(git -C "$DIR" rev-parse --abbrev-ref HEAD 2>/dev/null)

GREEN='\033[32m'; YELLOW='\033[33m'; RED='\033[31m'; CYAN='\033[36m'; BLUE='\033[34m'; MAGENTA='\033[35m'; RESET='\033[0m'

# Fixed per-model colour, keyed by substring so version bumps (e.g. "Opus 5"
# vs "Opus 4.8") still match.
case "$MODEL" in
    *Opus*)   MODEL_COLOR="$MAGENTA" ;;
    *Sonnet*) MODEL_COLOR="$BLUE" ;;
    *Haiku*)  MODEL_COLOR="$GREEN" ;;
    *Fable*)  MODEL_COLOR="$YELLOW" ;;
    *)        MODEL_COLOR="$RESET" ;;
esac

# Two-row context bar: 0-50% on top (blue fill, ▁ sits low), 51-100% on the
# bottom (red fill, ▔ sits high) — adjacent rows meet at the 50% boundary.
# 50 chars/row * 1%/char = 50 percentage points per row.
ROW_WIDTH=50
if [ "$PCT" -le 50 ]; then TOP=$PCT; BOTTOM=0; else TOP=50; BOTTOM=$((PCT - 50)); fi
TOP_FILLED=$TOP; TOP_EMPTY=$((ROW_WIDTH - TOP_FILLED))
BOTTOM_FILLED=$BOTTOM; BOTTOM_EMPTY=$((ROW_WIDTH - BOTTOM_FILLED))

repeat() { [ "$2" -gt 0 ] && printf -- "$1%.0s" $(seq 1 "$2"); }

TOP_FILL='▁'; TOP_TRACK='⣀'
BOTTOM_FILL='▔'; BOTTOM_TRACK='⠉'
TOP_BAR="${BLUE}$(repeat "$TOP_FILL" "$TOP_FILLED")${RESET}$(repeat "$TOP_TRACK" "$TOP_EMPTY")"
BOTTOM_BAR="${RED}$(repeat "$BOTTOM_FILL" "$BOTTOM_FILLED")${RESET}$(repeat "$BOTTOM_TRACK" "$BOTTOM_EMPTY")"

RATE_LINE=""
[ -n "$FIVE_HOUR" ] && RATE_LINE="5h: ${FIVE_HOUR}%"
[ -n "$SEVEN_DAY" ] && RATE_LINE="${RATE_LINE:+$RATE_LINE  }7d: ${SEVEN_DAY}%"

echo -e "[${MODEL_COLOR}${MODEL}${RESET}]${SESSION_NAME:+  🪪 ${CYAN}${SESSION_NAME}${RESET}}  |  📁 ${DIR##*/}${BRANCH:+  🌿 $BRANCH}"
[ -n "$RATE_LINE" ] && echo -e "$RATE_LINE"
echo -e "${TOP_BAR}"
echo -e "${BOTTOM_BAR}"
[ -n "$HARNESS_LINE" ] && echo -e "$HARNESS_LINE"
exit 0
