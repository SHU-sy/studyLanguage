import sys
input = sys.stdin.readline
n, k = map(int, input().split())
s = list(map(int, input().split()))
print(sorted(s)[n-k])