import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
ans = deque()
for i in range(n):
    command = input().split()
    if command[0] == "push":
        ans.append(command[1])
    elif command[0] == "pop":
        print(ans.popleft() if ans else "-1")
    elif command[0] == "size":
        print(len(ans))
    elif command[0] == "empty":
        print("0" if ans else "1")
    elif command[0] == "front":
        print(ans[0] if ans else "-1")
    else:
        print(ans[-1] if ans else "-1")