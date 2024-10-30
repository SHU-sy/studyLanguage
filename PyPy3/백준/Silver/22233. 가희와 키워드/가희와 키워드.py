import sys
input = sys.stdin.readline
keyw = set()

n, m = map(int, input().split())
for _ in range(n):
    keyw.add(input().strip())

for _ in range(m):
    blog = set(input().strip().split(","))
    keyw -= blog
    sys.stdout.write(f"{len(keyw)}\n")