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
    if root_a == root_b:
        return
    if costs[root_a] < costs[root_b]:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b

n, m, k = map(int, input().split())
costs = [0] + list(map(int, input().split()))
parent = [i for i in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)

roots = set()
for i in range(1, n+1):
    roots.add(find(i))

total = sum(costs[root] for root in roots)
print(total if total<=k else "Oh no")