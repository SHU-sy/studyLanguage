import sys
sys.setrecursionlimit(10**6)

def dfs(graph, x, y):
    graph[y][x] = 0
    for z in range(8):
        nx = x + dx[z]
        ny = y + dy[z]
        if 0<=nx<w and 0<=ny<h and graph[ny][nx] == 1:
            dfs(graph, nx, ny)


data = sys.stdin.read().splitlines()
idx = 0

dx = [0,0,1,-1,1,-1,1,-1]
dy = [1,-1,0,0,1,-1,-1,1]
result = []

while True:
    w, h = map(int, data[idx].split())
    if w == 0 and h == 0:
        break
    maps =  [list(map(int, line.split())) for line in data[idx+1:idx+h+1]]
    idx += h+1
    count = 0

    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1:
                dfs(maps, j, i)
                count += 1
    result.append(count)
for r in result:
    print(r)