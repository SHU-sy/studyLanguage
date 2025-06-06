import sys
sys.setrecursionlimit(10**6)
data = sys.stdin.read().splitlines()


def dfs(graph, start, visited):
    global cnt
    visited[start] = cnt
    cnt += 1
    for neighbor in graph[start]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)


n, m, r = map(int, data[0].split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
cnt = 1

idx = 1
for _ in range(m):
    u, v = map(int, data[idx].split())
    graph[u].append(v)
    graph[v].append(u)
    idx += 1

for u in range(1, n+1):
    graph[u].sort()

dfs(graph, r, visited)
print('\n'.join(map(str, visited[1:])))