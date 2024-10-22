import sys
from collections import deque
input = sys.stdin.readline
m = int(input())

for _ in range(m):
    command = deque(input().strip())
    left = deque()
    right = deque()

    while command:
        c = command.popleft()
        if c == "<":
            if not left:
                continue
            else:
                right.appendleft(left.pop())

        elif c == ">":
            if not right:
                continue
            else:
                left.append(right.popleft())

        elif c == "-":
            if left:
                left.pop()
            else:
                continue
        else:
            left.append(c)

    print("".join(left+right))