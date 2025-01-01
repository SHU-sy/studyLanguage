a, b = map(int, input().split())
money = a+b
c = int(input()) * 2

if money >= c:
    print(money-c)
else:
    print(money)