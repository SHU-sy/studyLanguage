import sys
input = sys.stdin.readline

n = int(input())
max_money = 0

for _ in range(n):
    money = 0
    a, b, c = map(int, input().split())
    if a==b and b==c:
        money = 10000 + a * 1000
    elif a==b or b==c:
        money = 1000 + b * 100
    elif a==c:
        money = 1000 + a * 100
    else:
        money = max(a, b, c) * 100

    max_money = max(max_money, money)
print(max_money)