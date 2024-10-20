import sys
import heapq
input = sys.stdin.readline
n = int(input())
num_heapq = []
for _ in range(n):
    num = int(input())
    if num == 0:
        if not num_heapq:
            print("0")
        else:
            print(heapq.heappop(num_heapq))
    else:
        heapq.heappush(num_heapq, num)