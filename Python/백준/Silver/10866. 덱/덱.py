import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
dq = deque()
for i in range(n):
    command = list(map(str, input().split()))

    match command[0]:
        case "push_front":
            dq.appendleft(command[1])
        case "push_back":
            dq.append(command[1])
        case "pop_front":
            print(dq.popleft() if dq else "-1")
        case "pop_back":
            print(dq.pop() if dq else "-1")
        case "size":
            print(len(dq))
        case "empty":
            print("0" if dq else "1")
        case "front":
            print(dq[0] if dq else "-1")
        case "back":
            print(dq[-1] if dq else "-1")