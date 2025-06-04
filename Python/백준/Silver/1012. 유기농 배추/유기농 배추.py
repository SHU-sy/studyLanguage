import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(graph, i, j):
    graph[i][j] = 0
    for a in range(4):
        ni = i + dy[a]
        nj = j + dx[a]
        if  0<=ni<n and 0<=nj<m and graph[ni][nj] == 1:
            dfs(graph, ni, nj)

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    count = 0

    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                dfs(graph, i, j)
                count += 1
    print(count)