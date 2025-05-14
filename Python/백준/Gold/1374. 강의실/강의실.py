import sys
import heapq
input = sys.stdin.readline

n = int(input())
lectures = sorted([tuple(map(int, input().split())) for _ in range(n)], key=lambda x: x[1])

end_times = []

for lecture in lectures:
    _, start, end = lecture

    if end_times and end_times[0] <= start:
        heapq.heappop(end_times)
    heapq.heappush(end_times, end)

print(len(end_times))