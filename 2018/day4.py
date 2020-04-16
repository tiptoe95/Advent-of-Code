from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path


input_path = Path.cwd() / 'inputs' / 'day4input.txt'
r = input_path.open('r').read()

guards = defaultdict(Counter)
for t, m in [l.split('] ') for l in sorted(r.splitlines()) if l]:
    t = datetime.strptime(t, '[%Y-%m-%d %H:%M')
    if '#' in m:
        g = int(m.split('#')[1].split()[0])
    if 'falls' in m:
        start = t
    if 'wakes' in m:
        minutes = int((t - start).total_seconds() // 60)
        guards[g].update(Counter((start.minute+i)%60 for i in range(minutes)))

_, id = max((sum(c.values()), id) for id, c in guards.items())
part1 = id * guards[id].most_common()[0][0]
print('part 1:', part1)

(_, minute), id = max((c.most_common()[0][::-1], id) for id, c in guards.items())
part2 = id * minute
print('part 2:', part2)
