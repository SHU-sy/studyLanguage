import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    data = deque(input().strip())
    count = 0
    val = True

    while data:
        temp = data.popleft()
        if temp == "(":
            count += 1
        elif temp == ")":
            count -= 1
        if count < 0:
            val = False
            break

    if count != 0:
        val = False

    print("YES" if val else "NO")