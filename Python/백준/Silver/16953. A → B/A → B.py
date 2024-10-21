import sys
a, b = map(int, sys.stdin.readline().split())
count = 1

while b > a:
    if b%2==0:
        b = b//2
        count += 1
    elif b%10==1:
        b = b//10
        count += 1
    else:
        break
if a == b:
    print(count)
else:
    print("-1")