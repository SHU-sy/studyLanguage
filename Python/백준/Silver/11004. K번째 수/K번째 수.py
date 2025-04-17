import sys
input = sys.stdin.readline

n, k = map(int, input().split())
num = sorted(list(map(int,input().split())))
print(num[k-1])