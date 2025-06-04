import sys
sys.setrecursionlimit(10**6)
data = sys.stdin.read().splitlines()
n = int(data[0])
maps = [list(map(int, line)) for line in data[1:]]

def dfs(graph, x, y):
    graph[y][x] = 0
    cnt = 1
    for z in range(4):
        nx = x + dx[z]
        ny = y + dy[z]
        if 0 <= nx < n and 0 <= ny < n and graph[ny][nx] == 1:
            cnt += dfs(graph, nx, ny)
    return cnt

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
result = []
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            result.append(dfs(maps, j, i))
print(len(result))
for num in sorted(result):
    print(num)