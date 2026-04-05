import sys
from collections import deque
input = sys.stdin.readline

def dfs(graph, start, visited, result):
    visited[start] = True
    result.append(start)
    for neighbor in graph[start]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, result)


def bfs(graph, start, visited):
    result = []
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
    return result


def main() -> None:
    n, m, v = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, n + 1):
        graph[i].sort()

    visited_dfs = [False] * (n+1)
    visited_bfs = [False] * (n+1)

    dfs_result = []
    dfs(graph, v, visited_dfs, dfs_result)
    bfs_result = bfs(graph, v, visited_bfs)

    print(" ".join(map(str, dfs_result)))
    print(" ".join(map(str, bfs_result)))

if __name__ == "__main__":
    sys.exit(main())