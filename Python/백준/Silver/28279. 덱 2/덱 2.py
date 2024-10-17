import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
ans = deque()
for i in range(n):
    p = list(map(int, input().split()))
    if p[0] == 1:
        ans.appendleft(p[1])
    if p[0] == 2:
        ans.append(p[1])
    if p[0] == 3:
        if ans:
            print(ans.popleft())
        else:
            print("-1")
    if p[0] == 4:
        if ans:
            print(ans.pop())
        else:
            print("-1")
    if p[0] == 5:
        print(len(ans))
    if p[0] == 6:
        if ans:
            print("0")
        else:
            print("1")
    if p[0] == 7:
        if ans:
            print(ans[0])
        else:
            print("-1")
    if p[0] == 8:
        if ans:
            print(ans[-1])
        else:
            print("-1")
