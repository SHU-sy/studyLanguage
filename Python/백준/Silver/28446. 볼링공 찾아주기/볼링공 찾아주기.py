import sys
input = sys.stdin.readline

n = int(input())
ball = {}

for _ in range(n):
    arr = list(map(int, input().split()))
    if arr[0] == 1:
        ball[arr[2]] = arr[1]

    elif arr[0] == 2:
        print(ball[arr[1]])