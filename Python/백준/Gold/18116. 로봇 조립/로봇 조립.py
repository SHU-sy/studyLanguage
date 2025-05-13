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
        size[root_a] += size[root_b]

n = int(input())
m = 10**6+1
parent = [i for i in range(m)]
size = [1]*m

for _ in range(n):
    cmd = input().split()
    if cmd[0] == "I":
        a = int(cmd[1])
        b = int(cmd[2])
        union(a, b)
    else:
        x = int(cmd[1])
        print(size[find(x)])