import sys
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    num = list(map(int, input().split()))
    if num[0] == 1:
        arr.append(num[1])
    if num[0] == 2:
        if arr:
            print(arr.pop())
        else:
            print("-1")
    if num[0] == 3:
        print(len(arr))
    if num[0] == 4:
        if not arr:
            print("1")
        else:
            print("0")
    if num[0] == 5:
        if arr:
            print(arr[-1])
        else:
            print("-1")
