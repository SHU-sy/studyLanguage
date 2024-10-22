import sys
from collections import deque
input = sys.stdin.readline
right = deque()
left = deque(input().strip())
m = int(input())

for _ in range(m):
    command = input().split()

    match command[0]:
        case "L":
            if not left:
                continue
            else:
                right.appendleft(left.pop())

        case "D":
            if not right:
                continue
            else:
                left.append(right.popleft())

        case "B":
            if not left:
                continue
            else:
                left.pop()

        case "P":
            left.append(command[1])
print("".join(left+right))