import sys
sys.setrecursionlimit(10**6)
lines = sys.stdin.read().splitlines()

def dfs(graph, i, j):
    count = 1
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    graph[i][j] = 0

    for k in range(4):
        ni = i + dx[k]
        nj = j + dy[k]
        if 0 <= ni < n and 0 <= nj < n and graph[ni][nj] == 1:
            count += dfs(graph, ni, nj)
    return count

n = int(lines[0])
graph = [list(map(int, line)) for line in lines[1:]]
result = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            result.append(dfs(graph, i, j))

print(len(result))
for r in sorted(result): print(r)