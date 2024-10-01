import sys
n, m = map(int, sys.stdin.readline().split())
p = [sys.stdin.readline().strip() for _ in range(n)]

p_index = {p[i]: i+1 for i in range(n)}

for i in range(m):
    q = sys.stdin.readline().strip()
    if q.isdigit():
        print(p[int(q)-1])

    else:
        if q in p_index:
            print(p_index[q])