import sys
import heapq
input = sys.stdin.readline
n = int(input())
lectures = sorted([tuple(map(int, input().split())) for _ in range(n)], key=lambda x: (x[0], x[1]))
end_heap = [lectures[0][1]]

for lecture in lectures[1:]:
    if end_heap and end_heap[0] <= lecture[0]:
        heapq.heappop(end_heap)
    heapq.heappush(end_heap, lecture[1])

print(len(end_heap))