import sys
import heapq
input = sys.stdin.readline

n = int(input())
card = [int(input()) for _ in range(n)]
heapq.heapify(card)
count = 0

while len(card) > 1:
    temp = heapq.heappop(card) + heapq.heappop(card)
    heapq.heappush(card, temp)
    count += temp
print(count)