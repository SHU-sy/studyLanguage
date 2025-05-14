import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_a != root_b:
        parent[root_b] = root_a

n, m = map(int, input().split())
parent = [i for i in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    if find(a) != find(b):
        union(a, b)
    else:
        print(i+1)
        sys.exit()
print(0)