import sys
input = sys.stdin.readline
sys.setrecursionlimit(200000)

def dfs (graph, node, visited, order, count):
    visited[node] = True
    order[node] = count[0]
    count[0] += 1

    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, order, count)


n, m, r = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n+1):
    graph[i].sort(reverse=True)

visited = [False] * (n+1)
order = [0] * (n+1)
count = [1]

dfs(graph, r, visited, order, count)

print("\n".join(map(str, order[1:])))