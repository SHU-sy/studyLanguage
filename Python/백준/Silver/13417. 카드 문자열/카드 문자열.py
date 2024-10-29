import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    card = input().split()
    ans = deque()

    for c in card:
        if not ans:
            ans.append(c)
        else:
            if c+"".join(ans) < "".join(ans)+c:
                ans.appendleft(c)
            else:
                ans.append(c)
    print("".join(ans))