import sys
input = sys.stdin.readline
n = int(input())
s= list(map(int, input().split()))
t, p = map(int, input().split())
c = 0
for size in s:
    c += (size+t-1)//t
print(c)
print(n//p, n%p)