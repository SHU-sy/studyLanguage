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

n = int(input())
parent = [i for i in range(n+1)]

for _ in range(n-2):
    a, b = map(int, input().split())
    union(a, b)

for i in range(1, n+1):
    for j in range(i+1, n+1):
        if find(i) != find(j):
            print(i, j)
            sys.exit()