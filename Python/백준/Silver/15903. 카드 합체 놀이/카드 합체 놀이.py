import heapq
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
min_num = list(map(int, input().split()))
heapq.heapify(min_num)

for _ in range(m):
    fir_num = heapq.heappop(min_num)
    sec_num = heapq.heappop(min_num)
    temp = fir_num + sec_num

    heapq.heappush(min_num, temp)
    heapq.heappush(min_num, temp)

print(sum(min_num))