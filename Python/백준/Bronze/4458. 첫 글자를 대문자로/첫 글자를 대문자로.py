import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    arr = input().strip()
    print(arr[0].upper()+arr[1:])