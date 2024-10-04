import sys
n = int(sys.stdin.readline().strip())
score = list(map(int, sys.stdin.readline().split()))
m = max(score)
s = sum(score)
print(s * 100 /m /n)