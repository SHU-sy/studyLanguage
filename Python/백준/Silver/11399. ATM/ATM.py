import sys
import heapq
input = sys.stdin.readline

n = int(input())
times = list(map(int, input().split()))
heapq.heapify(times)
total = 0
current = 0

while times:
    current += heapq.heappop(times)
    total += current
print(total)