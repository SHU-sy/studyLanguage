import sys
import heapq
input = sys.stdin.readline
n = int(input())
count = 1
lectures = sorted([tuple(map(int, input().split())) for _ in range(n)], key=lambda x: x[1])
end_heap = [lectures[0][2]]

for lecture in lectures[1:]:
    if end_heap and lecture[1] >= end_heap[0]:
        heapq.heappop(end_heap)

    heapq.heappush(end_heap, lecture[2])

    count = max(count, len(end_heap))
print(count)