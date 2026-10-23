"""For each text fragment, print file:line and the enclosing def of every match
in the harness CLI and harness-mail."""
import re, sys
FR = sys.argv[1:] or []
for path in ('setup/harness/bin/harness', 'setup/harness/bin/harness-mail'):
    src = open(path).read().splitlines()
    for frag in FR:
        for i, l in enumerate(src):
            if frag in l:
                j = i
                while j >= 0 and not re.match(r'\s*def \w+', src[j]): j -= 1
                fn = re.match(r'\s*def (\w+)', src[j]).group(1) if j >= 0 else '?'
                print(f'{frag[:40]!r:44s} {path.split("/")[-1]}:{i+1}  in {fn}()')
