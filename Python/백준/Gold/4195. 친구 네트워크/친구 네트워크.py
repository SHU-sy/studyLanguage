import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a_root = find(a)
    b_root = find(b)
    if a_root != b_root:
        parent[b_root] = a_root
        size[a_root] += size[b_root]

t = int(input())

for _ in range(t):
    f = int(input())
    parent = {}
    size = {}
    for _ in range(f):
        a, b = input().split()

        if a not in parent:
            parent[a] = a
            size[a] = 1
        if b not in parent:
            parent[b] = b
            size[b] = 1

        union(a, b)
        print(size[find(a)])