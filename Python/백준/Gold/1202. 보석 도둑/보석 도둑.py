import sys
import heapq
input = sys.stdin.readline

n, k = map(int, input().split())
juwels = [list(map(int, input().split())) for _ in range(n)]
juwels.sort(key=lambda x: x[0])

bags = sorted([int(input()) for _ in range(k)])

total = 0
heap = []
j_index = 0

for bag in bags:
    while j_index < n and juwels[j_index][0] <= bag:
        heapq.heappush(heap, -juwels[j_index][1])
        j_index += 1
    if heap:
        total += -heapq.heappop(heap)
print(total)