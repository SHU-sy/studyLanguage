import sys
from collections import deque
input = sys.stdin.readline

router = deque()
n = int(input())

while True:
    packet = int(input())

    if packet == -1:
        break

    elif packet == 0:
        router.popleft()

    else:
        router.append(packet)
print(" ".join(map(str, router)))