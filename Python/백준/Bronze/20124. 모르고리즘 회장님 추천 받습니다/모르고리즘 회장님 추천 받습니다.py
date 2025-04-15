import sys
input = sys.stdin.readline

n = int(input())
member = [(input().split()) for _ in range(n)]
ans = sorted(member, key=lambda x: (-int(x[1]), x[0]))
print(ans[0][0])