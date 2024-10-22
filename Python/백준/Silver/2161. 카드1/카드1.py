import sys
from collections import deque
n = int(sys.stdin.readline().strip())
card = deque([i+1 for i in range(n)])
ans = []
count = 1

while card:
    count += 1
    if count % 2 == 0:
        ans.append(card.popleft())
    else:
        card.rotate(-1)
print(" ".join(map(str, ans)))