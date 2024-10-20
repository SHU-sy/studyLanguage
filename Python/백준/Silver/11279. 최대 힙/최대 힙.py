import sys
import heapq
input = sys.stdin.readline
n = int(input())
num_heapq = []
for _ in range(n):
    num = int(input()) * -1
    if num == 0:
        if not num_heapq:
            print("0")
        else:
            print(heapq.heappop(num_heapq) * -1)
    else:
        heapq.heappush(num_heapq, num)