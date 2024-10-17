import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
ans = deque()
for i in range(n):
    p = list(map(int, input().split()))

    match p[0]:
        case 1:
            ans.appendleft(p[1])
        case 2:
            ans.append(p[1])
        case 3:
            if ans:
                print(ans.popleft())
            else:
                print("-1")
        case 4:
            if ans:
                print(ans.pop())
            else:
                print("-1")
        case 5:
            print(len(ans))
        case 6:
            if ans:
                print("0")
            else:
                print("1")
        case 7:
            if ans:
                print(ans[0])
            else:
                print("-1")
        case 8:
            if ans:
                print(ans[-1])
            else:
                print("-1")
