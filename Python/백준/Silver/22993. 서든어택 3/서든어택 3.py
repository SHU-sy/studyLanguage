import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

a1 = a[0]
attack = sorted(a[1:])

for player in attack:
    if a1 > player:
        a1 += player
    else:
        print("No")
        break
else:
    print("Yes")