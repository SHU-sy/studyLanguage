import sys
from collections import deque
lines = sys.stdin.read().splitlines()
n, m = map(int, lines[0].split())
maps = [list(map(int, line)) for line in lines[1:]]

def bfs(graph, x, y):
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<m and 0<=ny<n and graph[ny][nx]==1:
                queue.append((nx, ny))
                graph[ny][nx] = graph[y][x] + 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
bfs(maps, 0, 0)
print(maps[n-1][m-1])