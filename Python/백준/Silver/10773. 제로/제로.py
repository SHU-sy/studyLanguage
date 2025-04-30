import sys
input = sys.stdin.readline

k = int(input())
ans = []

for _ in range(k):
    num = int(input())
    if num != 0:
        ans.append(num)
    else:
        ans.pop()
print(sum(ans))