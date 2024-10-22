import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
where = deque(map(int, input().split()))
dq = deque([i for i in range(1, n+1)])
count = 0

for position in where:
    while True:
        if dq[0] == position:
            dq.popleft()
            break

        index = dq.index(position)

        if index <= len(dq)//2:
            dq.rotate(-1)

        else:
            dq.rotate(1)
        count += 1
print(count)