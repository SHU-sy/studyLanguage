from collections import deque
import sys
n, k = map(int, sys.stdin.readline().split())
people = deque([i+1 for i in range(n)])
ans = []

while people:
    people.rotate(-k)
    ans.append(people.pop())
print("<"+", ".join(map(str, ans))+">")