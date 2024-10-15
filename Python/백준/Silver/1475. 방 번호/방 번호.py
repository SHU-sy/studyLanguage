import sys
from collections import Counter
n = sys.stdin.readline().strip()
c = Counter(n)

c['6'] = (c['6'] + c['9'] + 1) // 2
del c['9']

print(max(c.values()))