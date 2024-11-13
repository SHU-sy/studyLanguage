import sys
input = sys.stdin.readline
sys.setrecursionlimit(200000)

def dfs (graph, node, visited, depth, current_d):
    visited[node] = True
    depth[node] = current_d

    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, depth, current_d+1)


n, m, r = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n+1):
    graph[i].sort()

visited = [False] * (n+1)
depth = [-1] * (n + 1)

dfs(graph, r, visited, depth, 0)

print("\n".join(map(str, depth[1:])))