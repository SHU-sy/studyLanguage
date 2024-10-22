import sys
import heapq
input = sys.stdin.readline

n = int(input())
meeting = sorted([tuple(map(int, input().split())) for _ in range(n)], key=lambda x: (x[0], x[1]))
end_heap = [meeting[0][1]]

for meet in meeting[1:]:
    if end_heap and end_heap[0] <= meet[0]:
        heapq.heappop(end_heap)
    heapq.heappush(end_heap, meet[1])

print(len(end_heap))