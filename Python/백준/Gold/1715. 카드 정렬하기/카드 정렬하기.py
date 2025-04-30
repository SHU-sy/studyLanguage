import sys
import heapq
input = sys.stdin.readline

n = int(input())
cards = [int(input()) for _ in range(n)]
heapq.heapify(cards)

total = 0
while len(cards) > 1:
    temp = heapq.heappop(cards) + heapq.heappop(cards)
    heapq.heappush(cards, temp)
    total += temp
print(total)