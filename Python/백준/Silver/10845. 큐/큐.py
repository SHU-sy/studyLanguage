import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
ans = deque()
for i in range(n):
    command = list(map(str, input().split()))
    match command[0]:
        case "push":
            ans.append(command[1])
        case "pop":
            print(ans.popleft() if ans else "-1")
        case "size":
            print(len(ans))
        case "empty":
            print("0" if ans else "1")
        case "front":
            print(ans[0] if ans else "-1")
        case "back":
            print(ans[-1] if ans else "-1")
