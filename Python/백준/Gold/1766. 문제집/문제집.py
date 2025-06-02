import sys, heapq
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0]*(n+1)
que = []
result = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

for i in range(1, n+1):
    if indegree[i] == 0:
        heapq.heappush(que, i)

while que:
    cur = heapq.heappop(que)
    result.append(cur)
    for node in graph[cur]:
        indegree[node] -= 1
        if indegree[node] == 0:
            heapq.heappush(que, node)
print(*result)