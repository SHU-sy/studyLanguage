from collections import deque
import sys
n, k, m = map(int, sys.stdin.readline().split())
people = deque([i+1 for i in range(n)])
ans = []
count = 0
direction = 1

while people:
    people.rotate(-k)
    ans.append(people.pop())
    count += 1

    if count % m == 0:
        people.reverse()
print("\n".join(map(str, ans)))