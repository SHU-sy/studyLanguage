import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
cards = deque(list(range(1, n+1)))

while True:
    if len(cards) == 1:
        print(cards[0])
        break
    cards.popleft()
    cards.rotate(-1)