import sys
n = int(sys.stdin.readline().strip())

sugar_count = 0

while n >= 0:
    if n % 5 == 0:
        sugar_count += n//5
        print(sugar_count)
        break
    n -= 3
    sugar_count += 1
else:
    print("-1")