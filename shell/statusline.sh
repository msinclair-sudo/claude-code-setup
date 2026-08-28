#!/bin/bash
# Claude Code statusline
# Line 1: model | 🏷️ session name (when known) | 📁 project folder | 🌿 git branch (when in a repo)
# Line 2: color-coded context bar with % | session duration
input=$(cat)

_parsed=$(echo "$input" | python3 -c "
import json, sys, os, glob
d = json.load(sys.stdin)
model = d.get('model', {}).get('display_name', '')
ws = d.get('workspace', {})
cdir = ws.get('project_dir') or ws.get('current_dir') or d.get('cwd', '')
pct = int(d.get('context_window', {}).get('used_percentage') or 0)
dur = int(d.get('cost', {}).get('total_duration_ms') or 0)
sid = d.get('session_id', '')

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

print(model)
print(cdir)
print(pct)
print(dur)
print(name)
")

MODEL=$(echo "$_parsed"    | sed -n '1p')
DIR=$(echo "$_parsed"      | sed -n '2p')
PCT=$(echo "$_parsed"      | sed -n '3p')
DURATION_MS=$(echo "$_parsed" | sed -n '4p')
SESSION_NAME=$(echo "$_parsed" | sed -n '5p')

BRANCH=$(git -C "$DIR" rev-parse --abbrev-ref HEAD 2>/dev/null)

GREEN='\033[32m'; YELLOW='\033[33m'; RED='\033[31m'; RESET='\033[0m'

if   [ "$PCT" -ge 90 ]; then BAR_COLOR="$RED"
elif [ "$PCT" -ge 70 ]; then BAR_COLOR="$YELLOW"
else BAR_COLOR="$GREEN"; fi

FILLED=$((PCT / 10)); EMPTY=$((10 - FILLED))
BAR=$(printf "%${FILLED}s" | tr ' ' '#')$(printf "%${EMPTY}s" | tr ' ' '-')

MINS=$((DURATION_MS / 60000)); SECS=$(((DURATION_MS % 60000) / 1000))

echo -e "[$MODEL]${SESSION_NAME:+  🏷️ $SESSION_NAME} 📁 ${DIR##*/}${BRANCH:+  🌿 $BRANCH}"
echo -e "${BAR_COLOR}${BAR}${RESET} ${PCT}% | ⏱️ ${MINS}m ${SECS}s"
