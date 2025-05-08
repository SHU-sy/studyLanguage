import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n+1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    find_a = find(a)
    find_b = find(b)
    if find_a != find_b:
        parent[find_b] = find_a

for _ in range(m):
    command, a, b = map(int, input().split())
    if command == 0:
        union(a, b)
    else:
        print("NO" if find(a) != find(b) else "YES")