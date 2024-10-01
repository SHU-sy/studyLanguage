from collections import deque
import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    p = deque(map(int, sys.stdin.readline().split()))
    c = 0
    p_index = deque(range(n))


    while p:
        if p[0] == max(p):
            c += 1
            p.popleft()
            if p_index.popleft() == m:
                print(c)
                break

        else:
            p.append(p.popleft())
            p_index.append(p_index.popleft())