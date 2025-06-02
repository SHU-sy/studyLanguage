import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
indgree = [0]*(n+1)
graph = [[] for _ in range(n+1)]
que = deque()
result = []

for _ in range(m):
    a, b = map(int ,input().split())
    indgree[b] += 1
    graph[a].append(b)

for i in range(1, n+1):
    if indgree[i] == 0:
        que.append(i)

while que:
    cur = que.popleft()
    result.append(cur)
    for node in graph[cur]:
        indgree[node] -= 1
        if indgree[node] == 0:
            que.append(node)
print(" ".join(map(str, result)))