import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

parent = [i for i in range(n+1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(i, j):
    find_i = find(i)
    find_j = find(j)
    if find_i != find_j:
        parent[find_j] = find_i

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 1:
            union(i+1, j+1)

plan = list(map(int, input().split()))
root = find(plan[0])
for city in plan:
    if find(city) != root:
        print("NO")
        break
else:
    print("YES")