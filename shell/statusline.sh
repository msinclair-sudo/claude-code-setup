#!/bin/bash
# Claude Code statusline
# Line 1: model | 📁 project folder | 🌿 git branch (when in a repo)
# Line 2: color-coded context bar with % | session duration
input=$(cat)

_parsed=$(echo "$input" | python3 -c "
import json, sys
d = json.load(sys.stdin)
model = d.get('model', {}).get('display_name', '')
ws = d.get('workspace', {})
cdir = ws.get('project_dir') or ws.get('current_dir') or d.get('cwd', '')
pct = int(d.get('context_window', {}).get('used_percentage') or 0)
dur = int(d.get('cost', {}).get('total_duration_ms') or 0)
print(model)
print(cdir)
print(pct)
print(dur)
")

MODEL=$(echo "$_parsed"    | sed -n '1p')
DIR=$(echo "$_parsed"      | sed -n '2p')
PCT=$(echo "$_parsed"      | sed -n '3p')
DURATION_MS=$(echo "$_parsed" | sed -n '4p')

BRANCH=$(git -C "$DIR" rev-parse --abbrev-ref HEAD 2>/dev/null)

GREEN='\033[32m'; YELLOW='\033[33m'; RED='\033[31m'; RESET='\033[0m'

if   [ "$PCT" -ge 90 ]; then BAR_COLOR="$RED"
elif [ "$PCT" -ge 70 ]; then BAR_COLOR="$YELLOW"
else BAR_COLOR="$GREEN"; fi

FILLED=$((PCT / 10)); EMPTY=$((10 - FILLED))
BAR=$(printf "%${FILLED}s" | tr ' ' '#')$(printf "%${EMPTY}s" | tr ' ' '-')

MINS=$((DURATION_MS / 60000)); SECS=$(((DURATION_MS % 60000) / 1000))

echo -e "[$MODEL] 📁 ${DIR##*/}${BRANCH:+  🌿 $BRANCH}"
echo -e "${BAR_COLOR}${BAR}${RESET} ${PCT}% | ⏱️ ${MINS}m ${SECS}s"
