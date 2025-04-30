import sys
import heapq
from collections import defaultdict
from heapq import heappush, heappop

input = sys.stdin.readline

n, k = map(int, input().split())
juwels = defaultdict(list)
for _ in range(n):
    m, v = map(int, input().split())
    juwels[m].append(v)

mass_list = sorted(juwels.keys())

bags = sorted([int(input()) for _ in range(k)])

total = 0
heap = []
j_index = 0
j_len = len(mass_list)

for bag in bags:
    while j_index < j_len and mass_list[j_index] <= bag:
        for juwel in juwels[mass_list[j_index]]:
            heappush(heap, -juwel)
        j_index += 1

    if heap:
        total += -heappop(heap)

print(total)