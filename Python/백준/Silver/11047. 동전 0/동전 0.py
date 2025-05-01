import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = sorted([int(input()) for _ in range(n)], reverse=True)

count = 0
for coin in coins:
    if k >= coin:
        count += k//coin
        k %= coin
print(count)