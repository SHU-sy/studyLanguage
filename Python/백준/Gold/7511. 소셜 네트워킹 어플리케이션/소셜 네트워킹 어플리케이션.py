import sys
input = sys.stdin.readline

t = int(input())

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_a != root_b:
        parent[root_b] = root_a

for i in range(1, t+1):
    print(f"Scenario {i}:")
    n = int(input())
    k = int(input())

    parent = [i for i in range(n+1)]

    for _ in range(k):
        a, b = map(int, input().split())
        union(a, b)

    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        print(0 if find(a)!= find(b) else 1)
    print("")