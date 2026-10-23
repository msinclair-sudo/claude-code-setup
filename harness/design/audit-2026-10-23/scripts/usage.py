"""Count `harness <sub> --flags` in Bash tool calls across biblion2 transcripts."""
import json, re, sys, glob, collections, pathlib, shlex
files = glob.glob(str(pathlib.Path.home() / ".claude/projects/*biblion2*/**/*.jsonl"), recursive=True)
subs = collections.Counter(); flags = collections.Counter(); first = {}; last = {}
pat = re.compile(r"(?:^|[\s;&|(`$])(?:\S*/)?harness\s+([a-z][a-z-]+)((?:\s+[^\s;&|]+)*)")
for f in files:
    for raw in open(f, errors="ignore"):
        if '"Bash"' not in raw or "harness" not in raw:
            continue
        try:
            d = json.loads(raw)
        except Exception:
            continue
        msg = d.get("message") or {}
        for c in msg.get("content") or []:
            if not isinstance(c, dict) or c.get("type") != "tool_use" or c.get("name") != "Bash":
                continue
            cmd = (c.get("input") or {}).get("command", "")
            for m in pat.finditer(cmd):
                s = m.group(1)
                subs[s] += 1
                ts = d.get("timestamp", "")
                first.setdefault(s, ts); last[s] = max(last.get(s, ""), ts)
                for fl in re.findall(r"\s(--[a-z][\w-]*)", m.group(2) or ""):
                    flags[f"{s} {fl}"] += 1
out = [f"# {len(files)} transcript files", "# subcommand count last_used"]
out += [f"{s} {n} {last.get(s,'')[:10]}" for s, n in subs.most_common()]
out += ["", "# subcommand flag count"]
out += [f"{k} {n}" for k, n in sorted(flags.items())]
pathlib.Path(sys.argv[1]).write_text("\n".join(out) + "\n")
print(len(files), sum(subs.values()))
