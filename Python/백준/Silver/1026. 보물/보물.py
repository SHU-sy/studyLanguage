import sys
input = sys.stdin.readline

n = int(input())
arr1 = sorted(map(int, input().split()))
arr2 = sorted(map(int, input().split()), reverse=True)
ans = 0
for i in range(n):
    ans += arr1[i] * arr2[i]
print(ans)