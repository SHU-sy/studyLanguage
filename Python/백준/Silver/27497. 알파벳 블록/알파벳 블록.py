import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
block = deque()
history = []

for i in range(n):
    button = list(input().split())
    if button[0] == "1":
        block.append(button[1])
        history.append(1)
    elif button[0] == "2":
        block.appendleft(button[1])
        history.append(2)
    elif button[0] == "3" and history:
        last = history.pop()
        if last == 1:
            block.pop()
        else:
            block.popleft()
if block:
    print("".join(block))
else:
    print("0")