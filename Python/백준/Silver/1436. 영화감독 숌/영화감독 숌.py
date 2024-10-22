import sys
n = int(input())
ans = []
for i in range(1000000000):
    if "666" in str(i):
        ans.append(i)
    if len(ans) == n:
        break
print(ans[n-1])