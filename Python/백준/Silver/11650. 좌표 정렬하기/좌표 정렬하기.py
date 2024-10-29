import sys
input = sys.stdin.readline

n = int(input())
p = [list(map(int, input().split())) for _ in range(n)]
ans = sorted(p, key=lambda x: (x[0], x[1]))
print("\n".join(f"{x[0]} {x[1]}" for x in ans))