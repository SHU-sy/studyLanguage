import sys
input = sys.stdin.readline

t = int(input())

def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(a, b, parent):
    root_a = find(a, parent)
    root_b = find(b, parent)
    if root_a != root_b:
        parent[root_b] = root_a

output = []
for i in range(1, t+1):
    output.append(f"Scenario {i}:")
    n = int(input())
    k = int(input())

    parent = [i for i in range(n+1)]

    for _ in range(k):
        a, b = map(int, input().split())
        union(a, b, parent)

    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        output.append("0" if find(a, parent)!= find(b, parent) else "1")
    output.append("")
print('\n'.join(output))