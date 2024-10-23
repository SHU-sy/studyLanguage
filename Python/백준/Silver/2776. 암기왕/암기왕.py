import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    num1 = set(map(int, input().split()))
    m = int(input())
    if_num = map(int, input().split())
    for count in if_num:
        print(1 if count in num1 else 0)
