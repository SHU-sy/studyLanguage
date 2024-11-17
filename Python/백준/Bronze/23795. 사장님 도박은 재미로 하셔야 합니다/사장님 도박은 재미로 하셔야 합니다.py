import sys
input = sys.stdin.readline
res = 0

while True:
    num = int(input())
    if num == -1:
        print(res)
        break

    res += num