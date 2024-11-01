import sys
from collections import defaultdict
input = sys.stdin.readline
ring_dict = defaultdict(list)
couple = []

n = int(input())
for _ in range(n):
    name, ring = input().split()
    if ring == "-":
        continue
    else:
        ring_dict[ring].append(name)

for name in ring_dict.values():
    if len(name) == 2:
        couple.append((name[0], name[1]))
print(len(couple))
for c in couple:
    print(c[0], c[1])