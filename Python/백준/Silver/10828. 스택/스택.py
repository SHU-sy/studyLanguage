import sys
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    a = list(map(str, input().split()))
    if a[0] == "push":
        arr.append(a[1])
    if a[0] == "pop":
        if not arr:
            print("-1")
        else:
            print(arr.pop())
    if a[0] == "size":
        print(len(arr))
    if a[0] == "empty":
        if arr:
            print("0")
        else:
            print("1")
    if a[0] == "top":
        if not arr:
            print("-1")
        else:
            print(arr[-1])