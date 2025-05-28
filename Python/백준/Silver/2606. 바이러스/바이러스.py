import sys
sys.setrecursionlimit(10**6)
data = list(map(int, sys.stdin.read().split()))

def dfs(graph, start, visited):
    visited[start] = True
    for neighbor in graph[start]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

computer = data[0]
node = data[1]
graph = [[] for _ in range(computer + 1)]

idx = 2
for _ in range(node):
    a, b = data[idx], data[idx+1]
    idx += 2
    graph[a].append(b)
    graph[b].append(a)

visited_dfs = [False] * (computer+1)
dfs(graph, 1, visited_dfs)
print(sum(visited_dfs) -1)