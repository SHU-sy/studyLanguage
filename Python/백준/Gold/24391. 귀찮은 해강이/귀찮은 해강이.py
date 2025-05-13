import sys
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
parent = [i for i in range(n+1)]

for _ in range(m):
    i, j = map(int, input().split())
    union(i, j)

n = list(map(int, input().split()))

current_class = n[0]
count = 0
for c in n[1:]:
    if find(current_class) != find(c):
        count += 1
    current_class = c
print(count)