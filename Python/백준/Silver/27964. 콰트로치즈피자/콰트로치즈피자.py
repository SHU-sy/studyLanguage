import sys
input = sys.stdin.readline
n = int(input())
cheese = input().split()
ans = set()
for c in cheese:
    if c.endswith("Cheese"):
        ans.add(c)
print("yummy" if len(ans)>=4 else "sad")