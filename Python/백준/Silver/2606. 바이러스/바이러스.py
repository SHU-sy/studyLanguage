import sys
input = sys.stdin.readline

def dfs(graph, start, visited):
    visited[start] = True
    for neighbor in graph[start]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

computer = int(input())
nodes = int(input())
graph = [[] for _ in range(computer+1)]
visited = [False] * (computer+1)

for _ in range(nodes):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
dfs(graph, 1, visited)
print(sum(visited)-1)